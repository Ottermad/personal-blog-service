from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
