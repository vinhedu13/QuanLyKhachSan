from datetime import datetime, date
import uuid

from sqlalchemy import and_

from QLKSWEBSITE import app, login
import paypalrestsdk
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy.model import Model
from sqlalchemy.exc import SQLAlchemyError

import dao
from flask import render_template, request, redirect, url_for, jsonify, flash, session
from QLKSWEBSITE import app, db, models, utils
from QLKSWEBSITE.dao import paypal, TaoPhieuDatPhong, taoID
from flask import render_template, request, redirect, url_for, flash
import utils


import hashlib
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
    data = dao.TimKiem(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, soLuong=int(soLuong))
    return render_template('search.html', data=data, soLuong=soLuong, ngayNhanPhong=ngayNhanPhong,
                           ngayTraPhong=ngayTraPhong)


@app.route("/datphong", methods=["GET", "POST"])
@login_required
def datphong():
    if request.method == "POST":
        idKhachHang = current_user.idKhachHang
        idLoaiPhong = request.form.get("id")
        soLuong = request.form.get("soLuong")
        ngaynhan = request.form.get('ngayNhanPhong')
        ngaytra = request.form.get('ngayTraPhong')
        thoiGianDat = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        loaiPhong = models.LoaiPhong.query.filter_by(id=idLoaiPhong).first()
        khachHang = models.KhachHang.query.filter_by(id=idKhachHang).first()
        tongTien = int(soLuong) * int(loaiPhong.donGia)
        print('ấdafafaf')

    return render_template("datphong.html", tongTien=tongTien, ngaynhan=ngaynhan,
                           thoiGianDat=thoiGianDat, idKhachHang=idKhachHang, idLoaiPhong=idLoaiPhong, soLuong=soLuong,
                           ngaytra=ngaytra, khachHang=khachHang)


@app.route("/thanhtoan", methods=['POST', 'GET'])
def thanhtoan():
    if request.method == "GET":
        thanhToan = request.args.get('payment')
        if session.get('loaiPhieu') == "phieuDat":
            print('if đặt')
            if dao.KiemTraThoiGianNhanPhong_DatPhong(thoiGianNhan=str(session.get('ngaynhan')),
                                                     thoiGianDat=str(session.get('thoiGianDat'))) <= 28:
                if thanhToan == 'paypal':
                    return redirect(url_for("paypal"))
                if thanhToan == 'momo':
                    return redirect(url_for("momo"))
            else:
                return render_template('search.html')
        if session.get('loaiPhieu') == "phieuThue":
            print(session.get('loaiPhieu'))
            print('if thuê')
            print(thanhToan)
            if thanhToan == 'paypal':
                return redirect(url_for("paypal"))
            if thanhToan == 'momo':
                return redirect(url_for("momo"))
    if request.method == "POST":
        session['email'] = request.form.get('email')
        session['hoTen'] = request.form.get('hoTen')
        session['loaiPhieu'] = request.form.get('loaiPhieu')
        session['tongTien'] = request.form.get('tongTien')
        session['ngaynhan'] = request.form.get('ngaynhan')
        session['ngaytra'] = request.form.get('ngaytra')
        session['thoiGianDat'] = request.form.get('thoiGianDat')
        session['idKhachHang'] = request.form.get('idKhachHang')
        session['idLoaiPhong'] = request.form.get("idLoaiPhong")
        session['soLuong'] = request.form.get("soLuong")
        session['ngayTraPhong'] = request.form.get("ngayTraPhong")
        session['khachHang'] = request.form.get('khachHang')
        session['phongDuocChon'] = request.form.get('phongDuocChon')
        idPhieu = request.form.get('idPhieu')
        print(session.get('phongDuocChon'))
        print(session.get('khachHang'))
        print('0000000000000')
        if dao.KiemTraThanhToan(idPhieu) == True:
            try:
                phieuDatPhong = models.PhieuDatPhong.query.filter_by(id=idPhieu).first()
                phieuDatPhong.trangThai = 'Đã nhận phòng'
                db.session.commit()
                phieuThuePhong = dao.TaoPhieuThuePhong(id=dao.taoID(), ngayNhanPhong=datetime.now(),
                                                       ngayTraPhong=session.get('ngayTraPhong'),
                                                       idPhieuDatPhong=idPhieu)
                khachHangTrongPhong = dao.TachDanhSachKhachHang(session.get('khachHang'))
                for k in khachHangTrongPhong:
                    loaiKhach = models.LoaiKhach.query.filter_by(tenLoaiKhach=k[2]).first()
                    khachHang = models.KhachHang(tenKhachHang=k[0], cccd=k[1], idLoaiKhach=loaiKhach.id)
                    khachHang = dao.TaoKhachHang(khachHang)
                    phieuThuePhong_Phong = dao.TaoPhieuThuePhong_Phong(idPhieuThuePhong=phieuThuePhong.id, idPhong=k[3])
                    # phieu_KhachHang = dao.TaoPhieu_KhachHang(idPhieu=phieuThuePhong.id, idKhachHang=khachHang.id)
                    phieuThuePhong_Phong_KhachHang = models.PhieuThuePhong_Phong_KhachHang(idKhachHang=khachHang.id,
                                                                                           idPhieuThuePhong_Phong=phieuThuePhong_Phong.id)
                    dao.TaoPhieuThuePhong_Phong_KhachHang(phieuThuePhong_Phong_KhachHang)
                print(f"Đã cập nhật trạng thái của phiếu {idPhieu} thành 'Đã nhận phòng'")
                return render_template('lapphieuthuephong_thanhcong.html')
            except Exception as e:
                # Rollback nếu có lỗi xảy ra
                db.session.rollback()
                print(f"Lỗi khi cập nhật trạng thái: {e}")

    return render_template('thanhtoan.html')


# @app.route("taophieuthue", methods=["POST", "GET"])
# def taophieuthue():
#

@app.route("/momo", methods=["GET", "POST"])
def momo():
    idPhieu = dao.taoID()
    tongTien = session.get('tongTien')
    tongTien = int(float(tongTien))
    print(idPhieu, tongTien, session.get('loaiPhieu'))
    return dao.ThanhToanMomo(idPhieu=idPhieu, tongTien=str(tongTien))


@app.route("/paypal", methods=["GET", "POST"])
def paypal():
    idPhieu = taoID()
    tongTien = session.get('tongTien')
    tongTien = float(tongTien)
    return dao.paypal(idPhieu=idPhieu, tongTien=int(tongTien))


# @app.route("/payment", methods=["POST"])
# def payment(idPhieuDatPhong):
#     hoaDon = models.HoaDon()
#     phieuDatPhong = models.PhieuDatPhong()
#     return dao.ThanhToanMomo(hoaDon.id, int(hoaDon.tongTien))


@app.route("/callbackmomo", methods=["POST"])
def callback():
    return dao.callbackmomo()


# @app.route('/payment/redirect', methods=['GET'])
# def payment_redirect():
#     # Xử lý thông tin trả về từ MoMo
#     response_data = request.args.to_dict()
#     # Kiểm tra trạng thái thanh toán và thực hiện các bước cần thiết
#     # (Lưu thông tin vào database, gửi email, v.v.)
#     return "Payment processed successfully!", 200


@app.route('/payment/redirect', methods=['GET'])
def payment_redirect():
    # Xử lý thông tin trả về từ MoMo
    data = request.args.to_dict()
    transId = data.get('transId')
    amount = data.get('amount')
    orderId = data.get('orderId')
    if str(session.get('loaiPhieu')) == "phieuDat":
        if current_user.idLoaiTaiKhoan == 2:
            dao.TaoPhieuDatPhong(id=int(orderId), idKhachHang=session.get('idKhachHang'),
                                 idLoaiPhong=session.get('idLoaiPhong'),
                                 soLuong=session.get('soLuong'), ngayNhanPhong=session.get('ngaynhan'),
                                 ngayTraPhong=session.get('ngaytra'))
            hoaDon = models.HoaDon(idPhieu=int(orderId), trangThai=1, tongTien=amount, thoiGianTao=datetime.now())
            db.session.add(hoaDon)
            db.session.commit()
        else:
            khachHang = models.KhachHang(tenKhachHang=session.get('hoTen'), email=session.get('email'))
            dao.TaoKhachHang(khachHang)
            dao.TaoPhieuDatPhong(id=int(orderId), idKhachHang=khachHang.id,
                                 idLoaiPhong=session.get('idLoaiPhong'),
                                 soLuong=session.get('soLuong'), ngayNhanPhong=session.get('ngaynhan'),
                                 ngayTraPhong=session.get('ngaytra'))
            hoaDon = models.HoaDon(idPhieu=int(orderId), trangThai=1, tongTien=amount, thoiGianTao=datetime.now())
            db.session.add(hoaDon)
            db.session.commit()
    if str(session.get('loaiPhieu')) == "phieuThue":
        phieuThuePhong = dao.TaoPhieuThuePhong(id=int(orderId), ngayNhanPhong=datetime.now(),
                                               ngayTraPhong=session.get('ngayTraPhong'))
        khachHangTrongPhong = dao.TachDanhSachKhachHang(session.get('khachHang'))
        for k in khachHangTrongPhong:
            loaiKhach = models.LoaiKhach.query.filter_by(tenLoaiKhach=k[2]).first()
            khachHang = models.KhachHang(tenKhachHang=k[0], cccd=k[1], idLoaiKhach=loaiKhach.id)
            khachHang = dao.TaoKhachHang(khachHang)
            phieuThuePhong_Phong = dao.TaoPhieuThuePhong_Phong(idPhieuThuePhong=phieuThuePhong.id, idPhong=k[3])
            # phieu_KhachHang = dao.TaoPhieu_KhachHang(idPhieu=phieuThuePhong.id, idKhachHang=khachHang.id)
            phieuThuePhong_Phong_KhachHang = models.PhieuThuePhong_Phong_KhachHang(idKhachHang=khachHang.id,
                                                                                   idPhieuThuePhong_Phong=phieuThuePhong_Phong.id)
            dao.TaoPhieuThuePhong_Phong_KhachHang(phieuThuePhong_Phong_KhachHang)
        hoaDon = models.HoaDon(idPhieu=int(orderId), trangThai=1, tongTien=amount, thoiGianTao=datetime.now())
        db.session.add(hoaDon)
        db.session.commit()
    return render_template('thanhtoanthanhcong.html')


# @app.route('/payment_success', methods=['GET'])
# def payment_success():
#     payment_id = request.args.get('paymentId')
#     payer_id = request.args.get('PayerID')
#     payment = paypalrestsdk.Payment.find(payment_id)
#     idPhieu = request.args.get('idPhieu')
#     tongTien = request.args.get('tongTien')
#     print(idPhieu)
#
#     if payment.execute({"payer_id": payer_id}):
#         hoaDon = models.HoaDon(idPhieu = idPhieu, trangThai = 1, tongTien = tongTien, thoiGianTao = datetime.now() )
#         db.session.add(hoaDon)
#         db.session.commit()
#         return jsonify({"message": "Payment executed successfully!", "payment": payment.to_dict()})
#     else:
#         return jsonify({"error": payment.error})

@app.route('/payment_success', methods=['GET'])
def payment_success():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)
    idPhieu = session.pop('idPhieu', None)
    tongTien = session.pop('tongTien', None)
    loaiPhieu = session.pop('loaiPhieuPaypal', None)
    print(idPhieu)
    if payment.execute({"payer_id": payer_id}):
        if str(session.get('loaiPhieu')) == "phieuDat":
            if current_user.idLoaiTaiKhoan == 2:
                dao.TaoPhieuDatPhong(id=int(idPhieu), idKhachHang=session.get('idKhachHang'),
                                     idLoaiPhong=session.get('idLoaiPhong'),
                                     soLuong=session.get('soLuong'), ngayNhanPhong=session.get('ngaynhan'),
                                     ngayTraPhong=session.get('ngaytra'))
                hoaDon = models.HoaDon(idPhieu=int(idPhieu), trangThai=1, tongTien=tongTien, thoiGianTao=datetime.now())
                db.session.add(hoaDon)
                db.session.commit()
                # query = (
                #     db.session.query(models.KhachHang.email)
                #     .join(models.PhieuDatPhong, models.KhachHang.id == models.PhieuDatPhong.idKhachHang)
                #     .filter(models.PhieuDatPhong.id == idPhieu)
                # )
                # result = query.first()
                # email = result[0]
                # subject = "Đặt phòng thành công - Mã đặt phòng: " + idPhieu
                # dao.GuiEmail(email, str(subject), str(subject))
            else:
                khachHang = models.KhachHang(tenKhachHang=session.get('hoTen'), email=session.get('email'))
                dao.TaoKhachHang(khachHang)
                dao.TaoPhieuDatPhong(id=int(idPhieu), idKhachHang=khachHang.id,
                                     idLoaiPhong=session.get('idLoaiPhong'),
                                     soLuong=session.get('soLuong'), ngayNhanPhong=session.get('ngaynhan'),
                                     ngayTraPhong=session.get('ngaytra'))
                hoaDon = models.HoaDon(idPhieu=int(idPhieu), trangThai=1, tongTien=tongTien, thoiGianTao=datetime.now())
                db.session.add(hoaDon)
                db.session.commit()
        if str(session.get('loaiPhieu')) == "phieuThue":
            phieuThuePhong = dao.TaoPhieuThuePhong(id=int(idPhieu), ngayNhanPhong=datetime.now(),
                                                   ngayTraPhong=session.get('ngayTraPhong'))
            khachHangTrongPhong = dao.TachDanhSachKhachHang(session.get('khachHang'))
            for k in khachHangTrongPhong:
                loaiKhach = models.LoaiKhach.query.filter_by(tenLoaiKhach=k[2]).first()
                khachHang = models.KhachHang(tenKhachHang=k[0], cccd=k[1], idLoaiKhach=loaiKhach.id)
                khachHang = dao.TaoKhachHang(khachHang)
                phieuThuePhong_Phong = dao.TaoPhieuThuePhong_Phong(idPhieuThuePhong=phieuThuePhong.id, idPhong=k[3])
                # phieu_KhachHang = dao.TaoPhieu_KhachHang(idPhieu=phieuThuePhong.id, idKhachHang=khachHang.id)
                phieuThuePhong_Phong_KhachHang = models.PhieuThuePhong_Phong_KhachHang(idKhachHang=khachHang.id,
                                                                                       idPhieuThuePhong_Phong=phieuThuePhong_Phong.id)
                dao.TaoPhieuThuePhong_Phong_KhachHang(phieuThuePhong_Phong_KhachHang)
            hoaDon = models.HoaDon(idPhieu=int(idPhieu), trangThai=1, tongTien=tongTien, thoiGianTao=datetime.now())
            db.session.add(hoaDon)
            db.session.commit()
        return render_template('thanhtoanthanhcong.html')
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


@app.route('/findOrder', methods=['GET'])
def find_order():
    phieuDatPhong = None
    maDatPhong = request.args.get("maDatPhong")
    if maDatPhong:
        phieuDatPhong = models.PhieuDatPhong.query.filter_by(id=maDatPhong)
    return render_template('find_order.html', phieuDatPhong=phieuDatPhong)


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


@app.route('/lapphieuthuephong', methods=['POST', 'GET'])
def kiemtrathuephong():
    loaiPhong = models.LoaiPhong.query.all()
    if request.method == 'POST':
        idPhieuDatPhong = request.form.get("idPhieuDatPhong")
        thoiGianTra = request.form.get("ngayTraPhong")
        thoiGianNhan = datetime.now()
        if idPhieuDatPhong:
            phieuDatPhong = models.PhieuDatPhong.query.get(idPhieuDatPhong)
            phongTrong = dao.DanhSachPhongTrong(phieuDatPhong.idLoaiPhong, thoiGianNhan, thoiGianTra)
        else:
            return render_template('find_order.html')
        return render_template('lapphieuthuephong.html', phongTrong=phongTrong, phieuDatPhong=phieuDatPhong,
                               thoiGianTra=thoiGianTra)
    if request.method == 'GET':
        idLoaiPhong = request.args.get('idLoaiPhong', 1)
        loaiPhongCheck = models.LoaiPhong.query.get(idLoaiPhong)
        thoiGianNhan = datetime.now()
        thoiGianTra = request.args.get('ngayTraPhong')
        if thoiGianTra == None:
            thoiGianTra = datetime.now()
        if thoiGianTra:
            phongTrong = dao.DanhSachPhongTrong(idLoaiPhong, thoiGianNhan, thoiGianTra)
        return render_template('lapphieuthuephong.html', loaiPhong=loaiPhong, idLoaiPhong=idLoaiPhong,
                               phongTrong=phongTrong, thoiGianTra=thoiGianTra, loaiPhongCheck=loaiPhongCheck)


@app.route('/lapphieuthuephong_thanhcong', methods=['GET', 'POST'])
def lapphieuthuephong():
    idLoaiPhong = request.args.get('idLoaiPhong')
    thoiGianNhan = datetime.now()
    thoiGianTra = request.args.get('ngayTraPhong')
    phong = request.args.get('phongDuocChon')
    khachHang = request.args.get('khachHang')
    khachHang = dao.TachDanhSachKhachHang(khachHang)
    # for khach in khachHang:
    # k = models.KhachHang(tenKhachHang = khach[0], cccd = khach[1])
    # db.session.add(k)
    # db.session.commit()
    print(khachHang)
    return render_template('lapphieuthuephong_thanhcong.html')


@app.route('/nhanvien', methods=['POST', 'GET'])
def nhanvien():
    thoiGianHienTai = '2024-12-23 15:00:00'
    phongDangSuDung = dao.GetPhongDangSuDung_ThoiGianTraPhongTuongUng(thoiGianHienTai=thoiGianHienTai)
    loaiPhong = models.LoaiPhong.query.all()
    phong = models.Phong.query.all()
    id = request.args.get('id')
    return render_template('nhanvien.html', phongDangSuDung=phongDangSuDung, loaiPhong=loaiPhong, id=id, phong=phong)


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    err_msg = ""
    if request.method.__eq__('POST'):
        name = request.form.get('name').strip()
        username = request.form.get('username').strip()
        phone = request.form.get('phone').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()
        confirm = request.form.get('comfirm').strip()

        if not name or not email or not password or not confirm or not username or not phone:
            err_msg = "Vui lòng điền đầy đủ tất cả các trường!"
        elif password != confirm:
            err_msg = "Mật khẩu không khớp!"
        else:
            try:

                utils.add_user(name=name, username=username, password=password, phone=phone, email=email)
                flash("Tạo tài khoản thành công! Vui lòng đăng nhập.", "success")
                return redirect(url_for('sign_up'))
            except Exception as ex:
                print(f"Lỗi: {ex}")
                err_msg = "Hệ thống gặp lỗi, vui lòng thử lại sau."

    return render_template('sign_in.html', err_msg=err_msg)

@app.route('/staff')
def staff():
    return render_template('nhanvien.html')

@app.route('/admin-redirect')
def admin_redirect():
    return redirect(url_for('admin.index'))

@app.route('/user-login', methods=['GET', 'POST'])
def user_signin():
    err_msg = ""
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username,password=password)

        if user and user.matKhau.__eq__(password):
            if user.idLoaiTaiKhoan == 1:
                return redirect(url_for('admin_redirect'))
            elif user.idLoaiTaiKhoan == 2:
                login_user(user)
                return redirect(url_for('index'))
            elif user.idLoaiTaiKhoan == 3:
                return redirect(url_for('staff'))
            else:
                err_msg = "Không xác định được loại tài khoản!"

        else:
            err_msg = 'Tên đăng nhập hoặc mật khẩu không chính xác!'

    return render_template('sign_in.html', err_msg=err_msg)


@app.route('/nhanvien-login', methods=['GET', 'POST'])
def nhanvien_signin():
    err_msg = ""
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password=password, role=3)
        if user:
            login_user(user=user)
        else:
            err_msg = 'Username hoặc password không chính xác!!!'

    return redirect(url_for('nhanvien'))


@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('index'))


@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route('/test')
def test():
    loaiPhong = models.LoaiPhong.query.all()
    idLoaiPhong = request.args.get('idLoaiPhong', 1)
    loaiPhongCheck = models.LoaiPhong.query.get(idLoaiPhong)
    thoiGianNhan = datetime.now()
    thoiGianTra = request.args.get('ngayTraPhong')
    if thoiGianTra == None:
        thoiGianTra = datetime.now()
    if thoiGianTra:
        phongTrong = dao.DanhSachPhongTrong(idLoaiPhong, thoiGianNhan, thoiGianTra)
    return render_template('test.html', loaiPhong=loaiPhong, idLoaiPhong=idLoaiPhong,
                           phongTrong=phongTrong, thoiGianTra=thoiGianTra, loaiPhongCheck=loaiPhongCheck)


# @app.route('/submit-customers', methods=['POST'])
# def submit_customers():
#     data = request.json  # Nhận dữ liệu JSON từ client
#     # Xử lý dữ liệu (lưu vào cơ sở dữ liệu, etc.)
#     for room in data:
#         room_id = room['roomId']
#         customers = room['customers']
#         # Xử lý từng khách hàng, ví dụ lưu vào cơ sở dữ liệu
#         print(f"Room ID: {room_id}, Customers: {customers}")
#
#     return jsonify({"message": "Dữ liệu đã được xử lý thành công!"}), 200

if __name__ == '__main__':
    from QLKSWEBSITE.admin import *

    with app.app_context():
        app.run(debug=True)
