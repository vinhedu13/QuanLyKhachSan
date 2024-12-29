import json, os

from flask import render_template

from sqlalchemy.sql.functions import user
from sqlalchemy.exc import SQLAlchemyError
from QLKSWEBSITE import db

from QLKSWEBSITE.models import TaiKhoan, KhachHang
import hashlib


def add_user(username, name, password, **kwargs):
        if not name or not password:
            raise ValueError("Tên và mật khẩu không được để trống!")


        hashed_password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        khachHang = KhachHang(tenKhachHang=username.strip())
        db.session.add(khachHang)
        db.session.flush()  # Đảm bảo lấy được id của KhachHang sau khi thêm

        user = TaiKhoan(
            idKhachHang=khachHang.id,
            ten=name,
            tenDangNhap=username,
            matKhau=password,
            soDienThoai=(kwargs.get('phone') or "").strip(),
            email=(kwargs.get('email') or "").strip()
        )

        db.session.add(user)
        db.session.commit()



# def check_login(username, password, role = None):
#     if username and password:
#         password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#
#         return TaiKhoan.query.filter(TaiKhoan.tenDangNhap.__eq__(username.strip()),
#                                  TaiKhoan.matKhau.__eq__(password)).first()


def check_login(username, password, role=None):
    u = TaiKhoan.query.filter_by(tenDangNhap=username.strip()).first()
    if u and u.matKhau.__eq__(password):
        if role:
            u = u.filter(TaiKhoan.idLoaiTaiKhoan.__eq__(role))
        return u
    return None


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)
