from app import db, app
import json, os
from app.models import TaiKhoan, KhachHang, ForeignKey
import hashlib
def count_cart(cart):
    total_quantity, total_amount = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity']*c['price']

    return {
        "total_quantity": total_quantity,
        "total_amount": total_amount
    }

def add_tk(username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    tk = TaiKhoan(username=username.strip(), password=password,
                  avatar=kwargs.get('avatar'))

    db.session.add(tk)
    db.session.commit()


def get_id_from_name(name):
    return TaiKhoan.query.filter(TaiKhoan.username.__eq__(name))
def tk_link_kh(tk_id, name, **kwargs):
    kh = KhachHang(tk_id=tk_id, name=name, email=kwargs.get('email'))
    db.session.add(kh)
    db.session.commit()

def check_login(username,password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                                    TaiKhoan.password.__eq__(password)).first()

def get_tk_by_id(tk_id):
    return TaiKhoan.query.get(tk_id)