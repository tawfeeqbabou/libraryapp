from application import db
from datetime import datetime

class Readers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reader_name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Books', backref='booksbr')

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(60))
    genre = db.Column(db.String(30))
    date_of_completion = db.Column(db.Date, nullable=False, default=datetime.now)
    reader_id = db.Column(db.Integer, db.ForeignKey('readers.id'), nullable=False)