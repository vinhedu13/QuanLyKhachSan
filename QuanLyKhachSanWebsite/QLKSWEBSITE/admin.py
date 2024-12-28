from flask_admin.form import Select2Widget

from QLKSWEBSITE import admin, db
from QLKSWEBSITE import app
from QLKSWEBSITE.models import KhachHang, TaiKhoan, LoaiTaiKhoan, LoaiKhach, Phong, LoaiPhong, TyLePhuThu, BaoCaoDoanhThu, BaoCaoThongKe, BaoCaoTanSuatSuDung
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
admin = Admin(app=app, name='Hệ Thống Quản Lý Khách', template_mode='bootstrap4')
class TaiKhoanModelView(ModelView):

    form_columns = ['ten', 'tenDangNhap', 'matKhau', 'soDienThoai', 'email', 'idLoaiTaiKhoan']  # Đảm bảo có idLoaiTaiKhoan ở đây

    # Thiết lập cho khóa ngoại idLoaiTaiKhoan, sẽ hiển thị giá trị từ bảng LoaiTaiKhoan
    form_widget_args = {
        'idLoaiTaiKhoan': {
            'widget': Select2Widget()  # Select2 widget giúp hiển thị dropdown
        }
    }

    form_args = {
        'idLoaiTaiKhoan': {
            'query_factory': lambda: db.session.query(LoaiTaiKhoan).all(),
            # Lấy tất cả các đối tượng từ bảng LoaiTaiKhoan
            'get_label': lambda c: c.tenLoaiTaiKhoan  # Cung cấp nhãn để hiển thị (ví dụ: tên loại tài khoản)
        }
    }

    # # Cách để tạo một dropdown tùy chỉnh cho khóa ngoại
    # def on_model_change(self, form, model, is_created):
    #     if is_created:
    #         model.idLoaiTaiKhoan = form.idLoaiTaiKhoan.data
    #     return super().on_model_change(form, model, is_created)


admin.add_view(ModelView(KhachHang, db.session))
admin.add_view(ModelView(LoaiKhach, db.session))
admin.add_view(TaiKhoanModelView(TaiKhoan, db.session))
admin.add_view(ModelView(LoaiTaiKhoan, db.session))
admin.add_view(ModelView(Phong, db.session))
admin.add_view(ModelView(LoaiPhong, db.session))
admin.add_view(ModelView(TyLePhuThu, db.session))


