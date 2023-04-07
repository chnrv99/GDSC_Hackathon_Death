from flask import Flask, request, jsonify
from keras.models import model_from_json
import numpy as np
from get_model import saved
import datetime
from pathlib import Path
from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy




model = saved()

# database code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///death.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class death(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    # city = db.Column(db.String(50))
    # addr = db.Column(db.String(200)) 
    # pin = db.Column(db.String(10))
    age = db.Column(db.String(3))
db.create_all()

def __init__(self, name, age):
    self.name = name
    # self.city = city
    # self.addr = addr
    # self.pin = pin
    self.age = age

@app.route('/leaderboard')
def show_all():
    return render_template('show_all.html', names = death.query.all())

@app.route("/")
def home():
    return render_template('forms_new.html')




@app.route("/predict", methods=["POST"])
def pred():
    name = str(request.form['name'])
    data1 = float(request.form['a'])
    data2 = float(request.form['b'])
    data3 = int(request.form['c'])
    data4 = float(request.form['d'])
    data5 = float(request.form['e'])
    data6 = float(request.form['f'])
    data7 = float(request.form['g'])
    data8 = float(request.form['h'])
    data9 = float(request.form['i'])

    


    arr = np.array(
        [[data1, data2, data3, data4, data5, data6, data7, data8, data9]])
    pred = model.predict(arr)

    pred_list = pred.tolist()



    # age1 = jsonify(pred_list)
    d_name = death(name = name,age =pred_list[0][0])
    db.session.add(d_name)
    db.session.commit()

    return jsonify(pred_list)
    


if __name__ == "__main__":
    app.run(debug=True)
