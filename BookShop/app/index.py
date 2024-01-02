import math

from flask import render_template, request, redirect
import dao
from app import app


@app.route('/')
def index():
    kw = request.args.get('kw')
    theloai_id = request.args.get('theloai_id')
    page = request.args.get("page")

    theloai = dao.load_theloai()
    sach = dao.load_sach(kw=kw, theloai_id = theloai_id, page=page)

    total = dao.count_sach()

    return render_template('index.html',theloai=theloai,
                           sach=sach,
                           pages=math.ceil(total / app.config['PAGE_SIZE']))


@app.route('/sach/<id>')
def details(id):
    sach_profile = dao.load_sachprofile(id)
    theloai_profile = dao.load_theloaiprofile(id)
    tacgia_profile = dao.load_tacgiaprofile(id)
    nxb_profile = dao.load_nxbrpofile(id)
    return render_template('details.html', sach_profile=sach_profile,theloai_profile=theloai_profile,
                           tacgia_profile=tacgia_profile,nxb_profile=nxb_profile)



if __name__ == '__main__':
    from app.admin import *
    app.run(debug=True)
