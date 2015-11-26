import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
	db.init_app(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)


if __name__ == '__main__':
	from blog import app
	with app.app_context():
		b = BlogPost.query.get(6)
		db.session.delete(b)
		db.session.commit()
