from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

class ReadersForm(FlaskForm):
    reader_name = StringField("Reader Name",validators = [DataRequired(), Length(max = 60)])
    submit = SubmitField("Submit")

class BooksForm(FlaskForm):
    book_title = StringField("Book Title",validators = [DataRequired(), Length(max = 60)])
    book_author = StringField("Book Author",validators = [DataRequired(), Length(max = 60)])
    genre = StringField("Genre",validators = [DataRequired(), Length(max = 60)])
    date_of_completion = DateField("Date Of Completion")
    submit = SubmitField("Submit")