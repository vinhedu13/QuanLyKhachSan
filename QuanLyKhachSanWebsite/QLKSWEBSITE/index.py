
from datetime import datetime, date
import uuid
import paypalrestsdk
from flask_sqlalchemy.model import Model
from sqlalchemy.exc import SQLAlchemyError

import dao
from flask import render_template, request, redirect, url_for, jsonify, flash
from QLKSWEBSITE import app, db, models
from QLKSWEBSITE.dao import callback_momo, paypal, TaoPhieuDatPhong


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/timkiem", methods=['GET', 'POST'])
def timkiem():
    ngayNhanPhong = request.form.get('ngayNhanPhong')
    ngayTraPhong = request.form.get('ngayTraPhong')
    ngayNhanPhong = ngayNhanPhong + " 14:00:00"
    ngayTraPhong = ngayTraPhong + " 12:00:00"
    soLuong = request.form.get('soLuong')
    soNguoi = 2
    data = dao.TimKiem(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, soLuong = int(soLuong), soNguoi = soNguoi)
    return render_template('search.html', data = data, soLuong = soLuong, ngayNhanPhong = ngayNhanPhong, ngayTraPhong = ngayTraPhong)

@app.route("/datphong", methods=["GET", "POST"])
def datphong():
    if request.method == "POST":
        idKhachHang = 1
        idLoaiPhong = request.form.get("id")
        soLuong = request.form.get("soLuong")
        ngaynhan = request.form.get('ngayNhanPhong')
        ngaytra = request.form.get('ngayTraPhong')
        thoiGianDat = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        loaiPhong = models.LoaiPhong.query.filter_by(id=idLoaiPhong).first()
        khachHang = models.KhachHang.query.filter_by(id=idKhachHang).first()
        tongTien = int(soLuong) * int(loaiPhong.donGia)

    return render_template("datphong.html", tongTien = tongTien, ngaynhan = ngaynhan,
                           thoiGianDat = thoiGianDat, idKhachHang = idKhachHang, idLoaiPhong = idLoaiPhong, soLuong = soLuong, ngaytra = ngaytra)


@app.route("/thanhtoan", methods=['POST'])
def thanhtoan():
    thanhToan = request.form.get('payment')
    tongTien = request.form.get('tongTien')
    ngaynhan = request.form.get('ngaynhan')
    ngaytra = request.form.get('ngaytra')
    thoiGianDat = request.form.get('thoiGianDat')
    idKhachHang = request.form.get('idKhachHang')
    idLoaiPhong = request.form.get("idLoaiPhong")
    soLuong = request.form.get("soLuong")
    if dao.KiemTraThoiGianNhanPhong_DatPhong(thoiGianNhan=str(ngaynhan), thoiGianDat=str(thoiGianDat)) <= 28:
        phieuDatPhong = dao.TaoPhieuDatPhong(idKhachHang= idKhachHang, idLoaiPhong=idLoaiPhong, soLuong=soLuong,
                                             ngayNhanPhong=ngaynhan, ngayTraPhong=ngaytra)
        if thanhToan == 'paypal':
            return redirect(url_for("paypal", tongTien=tongTien, idPhieu=phieuDatPhong.id))
        if thanhToan == 'momo':
            return redirect(url_for("momo", idPhieu=phieuDatPhong.id, tongTien=tongTien))
    else:
        return render_template('search.html')


# @app.route("taophieuthue", methods=["POST", "GET"])
# def taophieuthue():
#

@app.route("/momo", methods = ["GET", "POST"])
def momo():
    idPhieu = request.args.get("idPhieu")
    tongTien = request.args.get('tongTien')
    tongTien = int(float(tongTien))
    print(idPhieu, tongTien)
    return dao.ThanhToanMomo(idPhieu= idPhieu, tongTien = str(tongTien))

@app.route("/paypal", methods = ["GET", "POST"])
def paypal():
    idPhieu = request.args.get("idPhieu")
    tongTien = request.args.get('tongTien')
    tongTien = float(tongTien)
    return dao.paypal(idPhieu=idPhieu, tongTien=int(tongTien))


# @app.route("/payment", methods=["POST"])
# def payment(idPhieuDatPhong):
#     hoaDon = models.HoaDon()
#     phieuDatPhong = models.PhieuDatPhong()
#     return dao.ThanhToanMomo(hoaDon.id, int(hoaDon.tongTien))


@app.route("/callbackmomo", methods=["POST"])
def callback():
    return callback_momo()


@app.route('/payment/redirect', methods=['GET'])
def payment_redirect():
    # Xử lý thông tin trả về từ MoMo
    response_data = request.args.to_dict()
    # Kiểm tra trạng thái thanh toán và thực hiện các bước cần thiết
    # (Lưu thông tin vào database, gửi email, v.v.)
    return "Payment processed successfully!", 200


@app.route('/payment_success', methods=['GET'])
def payment_success():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)
    idPhieu = request.args.get('idPhieu')
    tongTien = request.args.get('tongTien')
    print(idPhieu)

    if payment.execute({"payer_id": payer_id}):
        hoaDon = models.HoaDon(idPhieu = idPhieu, trangThai = 1, tongTien = tongTien, thoiGianTao = datetime.now() )
        db.session.add(hoaDon)
        db.session.commit()
        return jsonify({"message": "Payment executed successfully!", "payment": payment.to_dict()})
    else:
        return jsonify({"error": payment.error})


@app.route('/payment_cancel', methods=['GET'])
def payment_cancel():
    return jsonify({"message": "Payment canceled by user!"})

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/discounts', methods=['GET', 'POST'])
def discount():
    return render_template('discounts.html')

@app.route('/find_order', methods=['GET', 'POST'])
def find_order():
    return render_template('find_order.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_in.html')

@app.route('/room/single')
def room_single():
    return render_template('room_single.html', room_name="Phòng Đơn", price=500000, details=[
        "Diện tích: 20m²",
        "Loại giường: 1 giường đơn",
        "Tiện ích: Wifi, điều hòa, TV, minibar",
    ])

@app.route('/room/double')
def room_double():
    return render_template('room_double.html', room_name="Phòng Đôi", price=800000, details=[
        "Diện tích: 30m²",
        "Loại giường: 1 giường đôi",
        "Tiện ích: Wifi, điều hòa, TV, minibar",
    ])

@app.route('/room/family')
def room_family():
    return render_template('room_family.html', room_name="Phòng Gia Đình", price=1200000, details=[
        "Diện tích: 40m²",
        "Loại giường: 2 giường đôi",
        "Tiện ích: Wifi, điều hòa, TV, minibar",
    ])

@app.route('/room/villa')
def room_villa():
    return render_template('room_villa.html', room_name="Villa", price=5000000, details=[
        "Diện tích: 120m²",
        "Loại giường: 4 giường đôi",
        "Tiện ích: Hồ bơi, bếp, không gian riêng tư",
    ])


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)