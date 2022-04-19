from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from datetime import datetime
from application import app, db
from flask import url_for, redirect
from application.models import Readers, Books

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:rememberpassword22-@10.91.48.3/flaskdb',
            SECRET_KEY='Test_Secret_Key',
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        db.create_all()
        reader1 = Readers(reader_name = "tawfeeq")
        reader2 = Readers(reader_name = "ross")
        book1 = Books(reader_id = 1, book_title = "Power Of Now", book_author = "Ekharte Tolle", genre = "self help")
        book2 = Books(reader_id = 2, book_title = "Quran", book_author = "Allah", genre = "religious")
        db.session.add(reader1)
        db.session.add(reader2)
        db.session.add(book1)
        db.session.add(book2)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestReader(TestBase):
    def test_reader_read(self):
        response = self.client.get(url_for('add_reader'))
        self.assertEqual(response.status_code, 200)

    def test_reader_create(self):
        response = self.client.post(
            url_for('add_reader'), 
            data = dict(reader_name = "tawfeeq"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_reader(self):
        response = self.client.get(url_for('delete_reader', read_id=1))
        self.assertNotIn(b"Log your completed books below and we'll keep track of them for you!", response.data)

    def test_edit_reader(self):
        response = self.client.post(url_for('edit_reader', read_id = 1),data = dict(reader_name = "jacamo"),follow_redirects = True)
        self.assertIn(b'jacamo', response.data)


class TestBook(TestBase):
    def test_book_read(self):
        response = self.client.get(url_for('add_book', read_id = 1))
        self.assertEqual(response.status_code, 200)

    def test_book_create(self):
        response = self.client.post(
            url_for('add_reader'), 
            data = dict(reader_name = "tawfeeq"),follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.client.get(url_for('delete_book', book_id=1))
        self.assertNotIn(b"Enter Your Book Title", response.data)