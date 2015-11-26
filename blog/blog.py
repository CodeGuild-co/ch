import os

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


@app.route('/')
def home():
	posts = BlogPost.query.all()
	return render_template('home.html', posts=posts)


@app.route('/writepost')
def writepost():
	return render_template('writepost.html')


@app.route('/savepost', methods=['POST'])
def savepost():
	title = request.form["title"]
	content = request.form["content"]
	b = BlogPost()
	b.title = title
	b.content = content
	db.session.add(b)
	db.session.commit()
	return redirect(url_for('posts', id=b.id))


@app.route('/posts/<int:id>/')
def posts(id):
    post = BlogPost.query.get(id)
    return render_template('post.html', title=post.title, content=post.content)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
