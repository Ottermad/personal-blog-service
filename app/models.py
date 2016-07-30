from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
