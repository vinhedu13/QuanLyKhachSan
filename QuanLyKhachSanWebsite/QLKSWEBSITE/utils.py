import json, os

from sqlalchemy.sql.functions import user

from QLKSWEBSITE import db
from QLKSWEBSITE.models import TaiKhoan, KhachHang
import hashlib


def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    khachHang = KhachHang(tenKhachHang = name.strip())
    db.session.add(khachHang)
    db.session.commit()
    user = TaiKhoan(idKhachHang = khachHang.id,
                tenDangNhap=username.strip(),
                matKhau=password,
                email=kwargs.get('email'))

    db.session.add(user)
    db.session.commit()


# def check_login(username, password, role = None):
#     if username and password:
#         password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#
#         return TaiKhoan.query.filter(TaiKhoan.tenDangNhap.__eq__(username.strip()),
#                                  TaiKhoan.matKhau.__eq__(password)).first()


def check_login(username, password, role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u = TaiKhoan.query.filter(TaiKhoan.tenDangNhap.__eq__(username.strip()),
                          TaiKhoan.matKhau.__eq__(password))
    if role:
        u = u.filter(TaiKhoan.idLoaiTaiKhoan.__eq__(role))

    return u.first()


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)