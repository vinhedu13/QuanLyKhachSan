import paypalrestsdk
from flask_sqlalchemy.model import Model

import dao
from flask import render_template, request, redirect, url_for, jsonify
from QLKSWEBSITE import app, models, db
from QLKSWEBSITE.dao import callback_momo, DatPhong


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/datphong", methods=["POST"])
def datphong():
    action = request.form.get("action")
    if action == 'paypal':
        return dao.DatPhong(action)
    if action == 'momo':
        return dao.DatPhong(action)


# @app.route("/payment", methods=["POST"])
# def payment(idPhieuDatPhong):
#     hoaDon = models.HoaDon()
#     phieuDatPhong = models.PhieuDatPhong()
#     return dao.ThanhToanMomo(hoaDon.id, int(hoaDon.tongTien))


@app.route("/callbackmomo", methods=["POST"])
def callback():
    return callback_momo()


@app.route('/payment/redirect', methods=['GET'])
def payment_redirect():
    # Xử lý thông tin trả về từ MoMo
    response_data = request.args.to_dict()
    # Kiểm tra trạng thái thanh toán và thực hiện các bước cần thiết
    # (Lưu thông tin vào database, gửi email, v.v.)
    return "Payment processed successfully!", 200


@app.route('/payment_success', methods=['GET'])
def payment_success():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)
    idHoaDon = request.args.get('idHoaDon')
    print(idHoaDon)

    if payment.execute({"payer_id": payer_id}):
        hoaDon = db.session.get(models.HoaDon, idHoaDon)
        hoaDon.trangThai = 1
        db.session.commit()
        return jsonify({"message": "Payment executed successfully!", "payment": payment.to_dict()})
    else:
        return jsonify({"error": payment.error})


@app.route('/payment_cancel', methods=['GET'])
def payment_cancel():
    return jsonify({"message": "Payment canceled by user!"})


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)