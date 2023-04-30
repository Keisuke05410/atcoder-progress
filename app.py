from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///progress.db'
db = SQLAlchemy(app)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(100), nullable=False)
    question_number = db.Column(db.Integer, nullable=False)
    correct = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Progress('{self.folder}', '{self.question_number}', '{self.correct}')"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder = request.form['folder']
        question_number = int(request.form['question_number'])
        correct = request.form.get('correct') == 'on'
        progress = Progress(folder=folder, question_number=question_number, correct=correct)
        db.session.add(progress)
        db.session.commit()
        return redirect(url_for('index'))

    progress_list = Progress.query.order_by(Progress.id).all()
    return render_template('index.html', progress_list=progress_list)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    progress = Progress.query.get(id)
    if progress:
        db.session.delete(progress)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
