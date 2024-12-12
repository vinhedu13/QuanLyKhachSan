import json
import uuid
from datetime import datetime, timedelta

import paypalrestsdk
import requests
import hmac
import hashlib
from flask import jsonify, request, url_for, redirect, render_template, render_template_string
from idna.idnadata import scripts
from sqlalchemy import and_, or_

from QLKSWEBSITE import db, models, app
from QLKSWEBSITE.models import LoaiPhong


def ThanhToanMomo(idPhieu, tongTien):
    # Thông tin thanh toán
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
    accessKey = "F8BBA842ECF85"
    secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
    orderInfo = "pay with MoMo"
    partnerCode = "MOMO"
    redirectUrl = "https://0ae3-222-253-45-135.ngrok-free.app/payment/redirect"
    ipnUrl = "https://0ae3-222-253-45-135.ngrok-free.app/callbackmomo"
    amount = str(tongTien)  # Số tiền thanh toán
    orderId = str(idPhieu)
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
            hoaDon = models.HoaDon(idPhieu = orderId, trangThai = 1, tongTien = amount, thoiGianTao = datetime.now())
            db.session.add(hoaDon)
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


def paypal(idPhieu, tongTien):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('payment_success', _external=True, idPhieu = idPhieu, tongTien = tongTien),
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


def KiemTraThoiGianNhanPhong_DatPhong(thoiGianNhan, thoiGianDat):
    thoiGianNhan = datetime.strptime(thoiGianNhan, '%Y-%m-%d %H:%M:%S')
    thoiGianDat = datetime.strptime(thoiGianDat, '%Y-%m-%d %H:%M:%S')
    khoangThoiGian = thoiGianNhan - thoiGianDat
    return khoangThoiGian.days


def KiemTraPhongTrongTheoThoiGian(idLoaiPhong, thoiGianNhan, thoiGianTra):
    danh_sach_phong = db.session.query(models.Phong).filter(models.Phong.idLoaiPhong == idLoaiPhong).all()
    phong_da_duoc_thue = (
        db.session.query(models.Phong.id)
        .join(models.PhieuThuePhong_Phong, models.Phong.id == models.PhieuThuePhong_Phong.idPhong)
        .join(models.PhieuThuePhong, models.PhieuThuePhong_Phong.idPhieuThuePhong == models.PhieuThuePhong.id)
        .filter(
            or_(
                and_(models.PhieuThuePhong.ngayNhanPhong <= thoiGianTra, models.PhieuThuePhong.ngayTraPhong > thoiGianNhan)
            )
        )
    ).distinct()

    danh_sach_phong_trong = [
        phong.id for phong in danh_sach_phong if phong.id not in {p.id for p in phong_da_duoc_thue}
    ]

    return danh_sach_phong_trong


def SoLuongPhongTrongTheoLoaiPhong(idLoaiPhong, thoiGianNhan, thoiGianTra):
    count = 0
    phongTrong = KiemTraPhongTrongTheoThoiGian(idLoaiPhong, thoiGianNhan, thoiGianTra)
    for phong in phongTrong:
        count = count + 1
    return count


def TaoPhieu(loaiPhieu):
    phieu = models.Phieu(loaiPhieu = loaiPhieu, thoiGianTao = datetime.now())
    db.session.add(phieu)
    db.session.commit()
    return phieu


def TaoPhieuDatPhong(idKhachHang, idLoaiPhong, soLuong):
    phieu = TaoPhieu(loaiPhieu= '2')
    phieuDatPhong = models.PhieuDatPhong(id = phieu.id, idLoaiPhong = idLoaiPhong, idKhachHang = idKhachHang, soLuong = soLuong )
    db.session.add(phieuDatPhong)
    db.session.commit()
    return phieuDatPhong


def TaoPhieuThuePhong_Phong(idPhieuThuePhong, idPhong):
    phieuThuePhong_Phong = models.PhieuThuePhong_Phong(idPhieuThuePhong=idPhieuThuePhong, idPhong=idPhong)
    db.session.add(phieuThuePhong_Phong)
    db.session.commit()
    return phieuThuePhong_Phong


def TaoPhieu_KhachHang(idKhachHang, idPhieu):
    phieu_KhachHang = models.Phieu_KhachHang(idPhieu = idPhieu, idKhachHang = idKhachHang)
    db.session.add(phieu_KhachHang)
    db.session.commit()
    return phieu_KhachHang


def TaoPhieuThuePhong(ngayNhanPhong, ngayTraPhong, idPhong, idKhachHang, idPhieuDatPhong):
    phieu = TaoPhieu(loaiPhieu= '1')
    phieuThuePhong = models.PhieuThuePhong(id = phieu.id, ngayNhanPhong = ngayNhanPhong, ngayTraPhong = ngayTraPhong, idPhieuDatPhong = idPhieuDatPhong)
    db.session.add(phieuThuePhong)
    db.session.commit()
    return phieuThuePhong


def TimKiem(ngayNhanPhong, ngayTraPhong, soNguoi, soPhong):
    ketQua = []
    listPhong = db.session.query(LoaiPhong).all()
    for p in listPhong:
        soPhongTrong = KiemTraPhongTrongTheoThoiGian(p.id, ngayNhanPhong, ngayTraPhong)
        ketQua.append({
            'tenLoaiPhong': listPhong.tenLoaiPhong,
            'donGia': listPhong.donGia,
            'soPhongCon': int(soPhongTrong),
        })




if __name__ == '__main__':
    with app.app_context():
        # a = KiemTraPhongTrongTheoThoiGian(1, '2024-12-01 14:00:00', '2024-12-05 12:00:00')
        # print(a)
        app.run(debug=True)
