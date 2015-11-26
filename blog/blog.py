from flask import Flask, render_template, redirect, url_for, request
import models
import json

app = Flask(__name__)

models.init_app(app)

@app.route('/')
def home():
	posts = models.BlogPost.query.all()
	return render_template('home.html', posts=posts)
def getallposts():
    data = ''
    fn = 'blog/posts.json'
    if getenv('DYNO') != None:
        fn = '/app/blog/posts.json'
    with open(fn, 'r') as f:
        data = f.read()
    return json.loads(data)

@app.route('/writepost')
def writepost():
	return render_template('writepost.html')


@app.route('/savepost', methods=['POST'])
def savepost():
	title = request.form["title"]
	content = request.form["content"]
	b = models.BlogPost()
	b.title = title
	b.content = content
	models.db.session.add(b)
	models.db.session.commit()
	return redirect(url_for('posts', id=b.id))


@app.route('/posts/<int:id>/')
def posts(id):
    post = models.BlogPost.query.get(id)
    return render_template('post.html', title=post.title, content=post.content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
