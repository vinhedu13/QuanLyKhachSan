import json, os

from sqlalchemy.sql.functions import user
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError
from QLKSWEBSITE import db
from QLKSWEBSITE.models import TaiKhoan, KhachHang
import hashlib


def add_user(name, password, **kwargs):
    try:
        # Kiểm tra dữ liệu đầu vào
        if not name or not password:
            raise ValueError("Tên và mật khẩu không được để trống!")

        # Băm mật khẩu bằng Werkzeug
        hashed_password = generate_password_hash(password.strip())

        # Tạo bản ghi KhachHang
        khachHang = KhachHang(tenKhachHang=name.strip())
        db.session.add(khachHang)
        db.session.flush()  # Đảm bảo lấy được id của KhachHang sau khi thêm

        # Tạo bản ghi TaiKhoan
        user = TaiKhoan(
            idKhachHang=khachHang.id,
            ten=name,
            matKhau=hashed_password,
            email=(kwargs.get('email') or "").strip()
        )
        print(name, password, kwargs.get('email'))

        db.session.add(user)

        # Commit tất cả thay đổi một lần
        db.session.commit()
    except ValueError as ve:
        print(f"Lỗi dữ liệu: {ve}")
        db.session.rollback()
        raise
    except SQLAlchemyError as sae:
        print(f"Lỗi cơ sở dữ liệu: {sae}")
        db.session.rollback()
        raise
    except Exception as ex:
        print(f"Lỗi không xác định: {ex}")
        db.session.rollback()
        raise


# def check_login(username, password, role = None):
#     if username and password:
#         password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#
#         return TaiKhoan.query.filter(TaiKhoan.tenDangNhap.__eq__(username.strip()),
#                                  TaiKhoan.matKhau.__eq__(password)).first()


def check_login(email, password, role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u = TaiKhoan.query.filter(TaiKhoan.email.__eq__(email.strip()),
                          TaiKhoan.matKhau.__eq__(password))
    if role:
        u = u.filter(TaiKhoan.idLoaiTaiKhoan.__eq__(role))

    return u.first()


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)