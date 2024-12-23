from QLKSWEBSITE import admin, db
from QLKSWEBSITE import app
from QLKSWEBSITE.models import KhachHang, TaiKhoan, Phieu, LoaiKhach, Phong, LoaiPhong
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
admin = Admin(app=app, name='Hệ Thống Quản Lý Khách', template_mode='bootstrap4')

admin.add_view(ModelView(KhachHang, db.session))
admin.add_view(ModelView(LoaiKhach, db.session))
admin.add_view(ModelView(TaiKhoan, db.session))
admin.add_view(ModelView(Phieu, db.session))
admin.add_view(ModelView(Phong, db.session))
admin.add_view(ModelView(LoaiPhong, db.session))


