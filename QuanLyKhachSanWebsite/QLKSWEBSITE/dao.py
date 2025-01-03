import json
import uuid
from datetime import datetime

import paypalrestsdk
import requests
import hmac
import hashlib
from flask import jsonify, request, url_for, redirect, render_template, render_template_string
from idna.idnadata import scripts
from sqlalchemy import and_

from QLKSWEBSITE import db, models, app


def ThanhToanMomo(idHoaDon, tongTien):
    # Thông tin thanh toán
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
    accessKey = "F8BBA842ECF85"
    secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
    orderInfo = "pay with MoMo"
    partnerCode = "MOMO"
    redirectUrl = "https://4ab1-115-76-97-74.ngrok-free.app/payment/redirect"
    ipnUrl = "https://4ab1-115-76-97-74.ngrok-free.app/callbackmomo"
    amount = str(tongTien)  # Số tiền thanh toán
    orderId = str(idHoaDon)
    requestId = str(uuid.uuid4())
    extraData = ""
    partnerName = "MoMo Payment"
    requestType = "payWithMethod"
    storeId = "Test Store"
    autoCapture = True
    lang = "vi"

    # Tạo chữ ký
    rawSignature = f"accessKey={accessKey}&amount={amount}&extraData={extraData}&ipnUrl={ipnUrl}&orderId={orderId}&orderInfo={orderInfo}&partnerCode={partnerCode}&redirectUrl={redirectUrl}&requestId={requestId}&requestType={requestType}"
    h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()

    # Tạo dữ liệu JSON để gửi
    data = {
        'partnerCode': partnerCode,
        'orderId': orderId,
        'partnerName': partnerName,
        'storeId': storeId,
        'ipnUrl': ipnUrl,
        'amount': amount,
        'lang': lang,
        'requestType': requestType,
        'redirectUrl': redirectUrl,
        'autoCapture': autoCapture,
        'orderInfo': orderInfo,
        'requestId': requestId,
        'extraData': extraData,
        'signature': signature
    }

    # Gửi yêu cầu đến MoMo
    response = requests.post(endpoint, json=data)

    # Kiểm tra phản hồi từ MoMo
    if response.status_code == 200:
        response_data = response.json()
        pay_url = response_data.get('payUrl')
        if pay_url:
            # Chuyển hướng người dùng đến payUrl
            return redirect(pay_url)
        else:
            return jsonify({'error': 'Pay URL not found in MoMo response'}), 400
    else:
        return jsonify({'error': 'Failed to connect to MoMo API', 'details': response.text}), 500


def callback_momo():
    try:
        # Lấy dữ liệu từ yêu cầu
        data = request.json
        if not data:
            return jsonify({'message': 'No data received'}), 400

        # Lưu dữ liệu từ MoMo vào các biến
        partnerCode = data.get('partnerCode')
        orderId = data.get('orderId')
        requestId = data.get('requestId')
        amount = data.get('amount')
        orderInfo = data.get('orderInfo')
        orderType = data.get('orderType')
        transId = data.get('transId')
        resultCode = data.get('resultCode')
        message = data.get('message')
        payType = data.get('payType')
        extraData = data.get('extraData')
        responseTime = data.get('responseTime')

        # Kiểm tra trạng thái thanh toán
        if resultCode == 0:  # 0 là thanh toán thành công
            print("Payment successful!")
            print(f"Transaction ID: {transId}, Amount: {amount}, Order ID: {orderId}")
            hoaDon = db.session.get(models.HoaDon, orderId)
            hoaDon.trangThai = 1
            db.session.commit()
        else:
            print(f"Payment failed. Result Code: {resultCode}, Message: {message}")

        # Tùy chọn: Lưu dữ liệu vào database hoặc xử lý logic khác
        # save_to_database(partnerCode, orderId, amount, transId, resultCode, message)

        # Phản hồi lại MoMo (quan trọng để MoMo biết rằng bạn đã nhận thông báo)
        return jsonify({'message': 'Callback received successfully'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'Internal Server Error'}), 500


def paypal(idHoaDon, tongTien):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('payment_success', _external=True, idHoaDon=idHoaDon),
            "cancel_url": url_for('payment_cancel', _external=True)
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Sample Item",
                    "sku": "item",
                    "price": str(int(tongTien / 25000)),
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(int(tongTien / 25000)),
                "currency": "USD"
            },
            "description": "This is a sample payment."
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                # Redirect khách hàng đến PayPal để thanh toán
                return redirect(link.href)
    else:
        return jsonify({"error": payment.error})


def KiemTraTinhTrangPhong_ThoiGianKhongQua28Ngay(idPhong, ngayNhanPhongMoi, ngayTraPhongMoi, ngayDatPhong):
    check = False
    ngayNhanPhongMoi = datetime.strptime(ngayNhanPhongMoi, '%Y-%m-%d %H:%M:%S')
    ngayTraPhongMoi = datetime.strptime(ngayTraPhongMoi, '%Y-%m-%d %H:%M:%S')
    if (ngayNhanPhongMoi - ngayDatPhong).days <= 28:
        check = True

    # Kiểm tra tình trạng phòng
    phong_trung = db.session.query(models.PhieuThuePhong).filter(
        models.PhieuThuePhong.idPhong == idPhong,
        and_(
            models.PhieuThuePhong.ngayNhanPhong <= ngayTraPhongMoi,
            models.PhieuThuePhong.ngayTraPhong >= ngayNhanPhongMoi
        )
    ).count()

    if phong_trung > 0:
        print("Phòng đã được đặt trong thời gian này, vui lòng chọn phòng khác hoặc thời gian khác.")
        check = False
    if phong_trung == 0:
        check = True

    return check


def TaoPhieuThue_PhieuDat_HoaDon_DatPhong(sdtNguoiDat, tenNguoiDat, emailNguoiDat, hoNguoiDat, thoiGianTao, idPhong,
                                          ngayNhanPhong, ngayTraPhong, trangThai, trangThaiHoaDon, tongTien):
    phieuThuePhong = models.PhieuThuePhong(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong,
                                           trangThai=trangThai,
                                           idPhong=idPhong, thoiGianTao=thoiGianTao)
    db.session.add(phieuThuePhong)
    db.session.commit()
    phieuDatPhong = models.PhieuDatPhong(id=phieuThuePhong.id, sdtNguoiDat=sdtNguoiDat, tenNguoiDat=tenNguoiDat,
                                         emailNguoiDat=emailNguoiDat,
                                         hoNguoiDat=hoNguoiDat, thoiGianTao=thoiGianTao)
    hoaDon = models.HoaDon(trangThai=trangThaiHoaDon, idPhieu=phieuThuePhong.id, thoiGianTao=thoiGianTao,
                           tongTien=tongTien)

    db.session.add(phieuDatPhong)
    db.session.add(hoaDon)
    db.session.commit()

    return hoaDon


def DatPhong(phuongThucThanhToan):
    sdtNguoiDat = "1234"
    tenNguoiDat = "Vinh"
    emailNguoiDat = "lqv@gmail.com"
    hoNguoiDat = "Lê"
    thoiGianTao = datetime.now()
    idPhong = '1'
    ngayNhanPhong = '2024-12-04 14:00:00'
    ngayTraPhong = '2024-12-05 14:00:00'
    trangThai = "Chưa nhận phòng"
    trangThaiHoaDon = 0
    tongTien = 90000

    if phuongThucThanhToan == 'momo':
        check = KiemTraTinhTrangPhong_ThoiGianKhongQua28Ngay(idPhong, ngayNhanPhong, ngayTraPhong, thoiGianTao)
        if check == True:
            create = TaoPhieuThue_PhieuDat_HoaDon_DatPhong(sdtNguoiDat, tenNguoiDat, emailNguoiDat, hoNguoiDat,
                                                           thoiGianTao,
                                                           idPhong,
                                                           ngayNhanPhong, ngayTraPhong, trangThai, trangThaiHoaDon,
                                                           tongTien)
            return ThanhToanMomo(create.id, int(create.tongTien))
        if check == False:
            return render_template("index.html")

    if phuongThucThanhToan == 'paypal':
        check = KiemTraTinhTrangPhong_ThoiGianKhongQua28Ngay(idPhong, ngayNhanPhong, ngayTraPhong, thoiGianTao)
        if check == True:
            create = TaoPhieuThue_PhieuDat_HoaDon_DatPhong(sdtNguoiDat, tenNguoiDat, emailNguoiDat, hoNguoiDat,
                                                           thoiGianTao,
                                                           idPhong,
                                                           ngayNhanPhong, ngayTraPhong, trangThai, trangThaiHoaDon,
                                                           tongTien)
            return paypal(create.id, int(create.tongTien))
        if check == False:
            return render_template("index.html")


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
