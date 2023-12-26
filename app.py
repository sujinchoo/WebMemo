from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memos.db'
db = SQLAlchemy(app)

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    memos = Memo.query.all()
    return render_template('index.html', memos=memos)

@app.route('/add_memo', methods=['POST'])
def add_memo():
    content = request.form.get('content')
    new_memo = Memo(content=content)
    db.session.add(new_memo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_memo/<int:memo_id>', methods=['GET', 'POST'])
def edit_memo(memo_id):
    memo = Memo.query.get(memo_id)

    if request.method == 'POST':
        memo.content = request.form.get('content')
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', memo=memo)

@app.route('/delete_memo/<int:memo_id>')
def delete_memo(memo_id):
    memo = Memo.query.get(memo_id)
    db.session.delete(memo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
