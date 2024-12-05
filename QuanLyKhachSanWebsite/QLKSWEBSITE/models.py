import os
from ctypes.wintypes import DOUBLE
from datetime import datetime
from email.policy import default
from more_itertools.recipes import unique
from pymysql.constants.FLAG import UNSIGNED
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, column, DOUBLE, DateTime, Enum
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship
from QLKSWEBSITE import db, app


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, info={"unsigned": True})



class TinhTrangPhong(BaseModel):
    __tablename__ = "tinhtrangphong"
    tenTinhTrangPhong = db.Column(db.String(50), nullable=True)
    def __str__(self):
        return self.tenTinhTrangPhong


class BaoCaoThongKe(BaseModel):
    __tablename__ = "baocaothongke"
    thoiGianTao = db.Column(db.DateTime, nullable=False, default=datetime.now())
    BaoCaoDoanhThu = relationship('BaoCaoDoanhThu', backref='baocaothongke', lazy=True)
    BaoCaoTanSuatSuDung = relationship('BaoCaoTanSuatSuDung', backref='baocaothongke', lazy=True)
    trangThai = db.Column(db.Boolean, nullable=False, default= True )


class BaoCaoDoanhThu(db.Model):
    __tablename__ = "baocaodoanhthu"
    id = db.Column(db.Integer, ForeignKey('baocaothongke.id'), primary_key=True, autoincrement=True, nullable=False, info={"unsigned": True})
    doanhThu = db.Column(db.Double, nullable=False)


class BaoCaoTanSuatSuDung(db.Model):
    __tablename__ = "baocaotansuatsudung"
    id = db.Column(db.Integer, ForeignKey('baocaothongke.id'),primary_key=True, nullable=False, info={"unsigned": True})
    soLuotThue = db.Column(db.Integer, nullable=False)


class KhachHang(BaseModel):
    __tablename__ = "khachhang"
    tenKhachHang = db.Column(db.String(50), nullable=True)
    hoKhachHang = db.Column(db.String(50), nullable=True)
    gioiTinh = db.Column(db.Enum('Nam','Nữ'), nullable=True)
    cccd = db.Column(db.String(12), nullable=True)
    quocTich = db.Column(db.Integer, ForeignKey('quoctich.id'), nullable=True, info={"unsigned": True})
    sdt = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    diaChi = db.Column(db.String(200), nullable=True)
    idLoaiKhach = db.Column(db.Integer, ForeignKey('loaikhach.id'), nullable=True, info={"unsigned": True})
    phieu_khachhang = relationship('Phieu_KhachHang', backref='khachhang', lazy=True)
    taikhoan = relationship('TaiKhoan', backref='khachhang', lazy=True)
    def __str__(self):
        return (
            f"Khách hàng: {self.hoKhachHang} {self.tenKhachHang}, "
            f"Giới tính: {self.gioiTinh}, "
            f"CCCD: {self.cccd}, "
            f"Quốc tịch: {self.quocTich}, "
            f"SDT: {self.sdt}, "
            f"Email: {self.email}, "
            f"Địa chỉ: {self.diaChi}"
            f"Loại Khách: {self.idLoaiKhach}"
        )


class LoaiPhong(BaseModel):
    __tablename__ = "loaiphong"
    tenLoaiPhong = db.Column(db.String(50), nullable=False)
    donGia = db.Column(db.Double, nullable=False)
    phong = relationship('Phong', backref='loaiphong', lazy=True)
    def __str__(self):
        return self.tenLoaiPhong


class Phong(BaseModel):
    __tablename__ = "phong"
    tenPhong = db.Column(db.String(50), nullable=False)
    idLoaiPhong = db.Column(db.Integer, ForeignKey('loaiphong.id'), nullable=False, info={"unsigned": True})
    idTinhTrangPhong = db.Column(db.Integer, ForeignKey('tinhtrangphong.id'), nullable=False, info={"unsigned": True})
    phieuthuephong = relationship('PhieuThuePhong', backref='phong', lazy=True)
    def __str__(self):
        return self.tenPhong


class PhieuThuePhong(BaseModel):
    __tablename__ = "phieuthuephong"
    idPhong = db.Column(db.Integer, ForeignKey('phong.id'), nullable=False, info={"unsigned": True})
    ngayNhanPhong = db.Column(db.DateTime, nullable=False)
    ngayTraPhong = db.Column(db.DateTime, nullable=False)
    thoiGianTao = db.Column(db.DateTime, nullable=False, default = datetime.now())
    trangThai = db.Column(db.Enum('Đã nhận phòng','Chưa nhận phòng','Đã hủy', 'Quá hạn nhận'), nullable=False)
    hoadon = relationship('HoaDon', backref='phieuthuephong', lazy=True)
    phieudatphong = relationship('PhieuDatPhong', backref='phieuthuephong', lazy=True)
    phieu_khachhang = relationship('Phieu_KhachHang', backref='phieuthuephong', lazy=True)


class HoaDon(BaseModel):
    __tablename__ = "hoadon"
    tongTien = db.Column(db.Double, nullable=False)
    trangThai = db.Column(db.Boolean, nullable=False, default = False)
    idPhieu = db.Column(db.Integer, ForeignKey('phieuthuephong.id'), nullable=False, info={"unsigned": True}, unique = True)
    thoiGianTao = db.Column(db.DateTime, nullable=False, default = datetime.now())
    thanhtoan = relationship('ThanhToan', backref='hoadon', lazy=True)
    baocaothongke_hoadon = relationship('BaoCaoThongKe_HoaDon', backref='hoadon', lazy=True)



class QuocTich(BaseModel):
    __tablename__ = "quoctich"
    tenQuocTich = db.Column(db.String(50), nullable=False)
    khachhang = relationship('KhachHang', backref='quoctich', lazy=True)
    def __str__(self):
        return self.tenQuocTich


class TaiKhoan(BaseModel):
    __tablename__ = "taikhoan"
    tenDangNhap = db.Column(db.String(50), nullable=False)
    matKhau = db.Column(db.String(50), nullable=False)
    sdt = db.Column(db.String(15), nullable=False)
    thoiGianTao = db.Column(db.DateTime, nullable=False, default = datetime.now())
    idRole = db.Column(db.Integer, ForeignKey('loaitaikhoan.id'), nullable=False, info={"unsigned": True})
    thongtin = db.Column(db.Integer, ForeignKey('khachhang.id'), nullable=False, info={"unsigned": True}, unique = True)


class LoaiTaiKhoan(BaseModel):
    __tablename__ = "loaitaikhoan"
    tenLoaiTaiKhoan = db.Column(db.String(50), nullable=False)
    taikhoan = relationship('TaiKhoan', backref='loaitaikhoan', lazy=True)
    def __str__(self):
        return self.tenLoaiTaiKhoan


class Phieu_KhachHang(BaseModel):
    __tablename__ = "phieu_khachhang"
    idKhachHang = db.Column(db.Integer, ForeignKey('khachhang.id'), nullable=False, info={"unsigned": True})
    idPhieu = db.Column(db.Integer, ForeignKey('phieuthuephong.id'), nullable=False, info={"unsigned": True})


class PhieuDatPhong(db.Model):
    __tablename__ = "phieudatphong"
    id = db.Column(db.Integer, ForeignKey('phieuthuephong.id'),primary_key=True, nullable=False, info={"unsigned": True})
    thoiGianTao = db.Column(db.DateTime, nullable=False, default = datetime.now())
    tenNguoiDat = db.Column(db.String(50), nullable=False)
    hoNguoiDat = db.Column(db.String(50), nullable=False)
    emailNguoiDat = db.Column(db.String(50), nullable=False)
    sdtNguoiDat = db.Column(db.String(15), nullable=False)


class ThanhToan(BaseModel):
    __tablename__ = "thanhtoan"
    idHoaDon = db.Column(db.Integer, ForeignKey('hoadon.id'), nullable=False, info={"unsigned": True}, unique = True)
    thoiGianTao = db.Column(db.DateTime, nullable=False, default = datetime.now())



class BaoCaoThongKe_HoaDon(BaseModel):
    __tablename__ = "baocaothongke_hoadon"
    idBaoCaoThongKe = db.Column(db.Integer, ForeignKey('baocaothongke.id'), nullable=False, info={"unsigned": True})
    idHoaDon = db.Column(db.Integer, ForeignKey('hoadon.id'), nullable=False, info={"unsigned": True})


class LoaiKhach(BaseModel):
    __tablename__ = "loaikhach"
    tenLoaiKhach = db.Column(db.String(50), nullable=False)
    khachhang = relationship('KhachHang', backref='loaikhach', lazy=True)
    def __str__(self):
        return self.tenLoaiKhach


def them():
    a = LoaiKhach(tenLoaiKhach='Siêu VIP')
    db.session.add(a)
    db.session.commit()
    print("Thêm dữ liệu thành công!")


if __name__ == '__main__':
    with app.app_context():
        app.run(debug = True)

