from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///progress.db'
db = SQLAlchemy(app)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    alphabet = db.Column(db.String(100), nullable=False)
    correct = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['URL']
        url = url.split('/')[-1]
        name = url[:3]
        number = int(url[3:6])
        alphabet = url[-1]
        correct = request.form['correct']
        date = datetime.datetime.now()
        progress = Progress(name=name, number=number, alphabet=alphabet, correct=correct, date=date)
        db.session.add(progress)
        db.session.commit()
        return redirect("/")

    progress_list = Progress.query.order_by(Progress.id).all()
    return render_template('index.html', progress_list=progress_list)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == "GET":
        progress_list = Progress.query.order_by(Progress.id).all()
        return render_template("edit.html", progress_list=progress_list, id=id)
    else:
        progress = Progress.query.get(id)
        progress.name = request.form['name']
        progress.number = int(request.form['number'])
        progress.alphabet = request.form['alphabet']
        progress.correct = True if request.form['correct'] == 'correct' else False
        progress.date = datetime.datetime.now()
        db.session.commit()
        return redirect("/")

@app.route("/try/<int:id>", methods=['GET', 'POST'])
def try_edit(id):
    if request.method == "GET":
        progress_list = Progress.query.order_by(Progress.id).all()
        return render_template("try.html", progress_list=progress_list, id=id)
    else:
        progress = Progress.query.get(id)
        if request.form['correct_try'] == 'correct':
            progress.correct = "wrong before"
        progress.date = datetime.datetime.now()
        db.session.commit()
        return redirect("/")

@app.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    if request.method=="GET":
        progress = Progress.query.get(id)
        db.session.delete(progress)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
