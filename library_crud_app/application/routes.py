from application import app, db
from flask import request, redirect, render_template, url_for
from application.models import Readers, Books
from application.forms import ReadersForm, BooksForm

# Home app route
@app.route("/")
def index():
    all_readers = Readers.query.all()
    return render_template("index.html", all_readers = all_readers)

# App route adds reader
@app.route("/add_reader", methods=["GET", "POST"])
def add_reader():
    form = ReadersForm()
# if the method is post then the form will be committed to the database
    if request.method == "POST":
        reader = Readers(reader_name = form.reader_name.data)
        db.session.add(reader)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add_reader.html", form = form)

# Adding book with reader id
@app.route("/add_book/<int:read_id>", methods=["GET", "POST"])
def add_book(read_id):
    form = BooksForm()
# if the method is post then the form will be committed to the database
    if request.method == "POST":
        books = Books(reader_id = read_id, book_title = form.book_title.data, book_author = form.book_author.data, 
                    genre = form.genre.data, date_of_completion = form.date_of_completion.data)

        db.session.add(books)
        db.session.commit()
        return redirect(url_for("reader_books", read_id = read_id))

    return render_template("add_book.html", form = form)

# Viewing book added
@app.route("/reader_books/<int:read_id>")
def reader_books(read_id):
    all_books = Books.query.filter_by(reader_id=read_id).all()
    return render_template("reader_books.html", all_books = all_books)

@app.route("/edit_reader/<int:read_id>", methods = ["GET", "POST"])
def edit_reader(read_id):
    reader = Readers.query.get(read_id)
    form = ReadersForm()

    if request.method == "POST":
        reader.reader_name = form.reader_name.data
        db.session.commit()
        return redirect(url_for("index"))

    form.reader_name.data = reader.reader_name

    return render_template("add_reader.html", form = form)

@app.route("/delete_reader/<int:read_id>")
def delete_reader(read_id):
    reader = Readers.query.get(read_id)
    db.session.delete(reader)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_book/<int:book_id>', methods = ['GET', 'POST'])
def edit_book(book_id):
    books = Books.query.get(book_id)
    form = BooksForm()

    if request.method == "POST":
        books.book_title = form.book_title.data
        books.book_author = form.book_author.data
        books.genre = form.genre.data
        books.date_of_completion = form.date_of_completion.data
        db.session.commit()
        return redirect(url_for('index'))

    form.book_title.data = books.book_title
    form.book_author.data = books.book_author
    form.genre.data = books.genre
    form.date_of_completion.data = books.date_of_completion

    return render_template('add_book.html', form = form)

@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    books = Books.query.get(book_id)
    db.session.delete(books)
    db.session.commit()
    return redirect(url_for('index'))