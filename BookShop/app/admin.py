from app import app, db
from flask_admin import Admin
from app.models import Sach, TheLoai, NhaXuatBan, TacGia
from flask_admin.contrib.sqla import ModelView

admin =Admin (app=app, name="Bookshop Administrator", template_mode='bootstrap4')
admin.add_view(ModelView(Sach, db.session))
admin.add_view(ModelView(TheLoai, db.session))
admin.add_view(ModelView(NhaXuatBan, db.session))
admin.add_view(ModelView(TacGia, db.session))