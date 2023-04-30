from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///progress.db'
db = SQLAlchemy(app)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(100), nullable=False)
    question_number = db.Column(db.Integer, nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder = request.form['folder']
        question_number = int(request.form['question_number'])
        correct = request.form.get('correct') == 'on'
        date = datetime.datetime.now()
        progress = Progress(folder=folder, question_number=question_number, correct=correct, date=date)
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
        progress.folder = request.form['folder']
        progress.question_number = int(request.form['question_number'])
        progress.correct = request.form.get('correct') == 'on'
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
