from flask import Flask, render_template, request, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Creating database named books.db

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db = SQLAlchemy(app)

# clas model with author title and publication year 
class Book(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column("title", db.String(100), nullable = False)
    author = db.Column("author", db.String(100), nullable = False)
    publication_year = db.Column("publication_year", db.Integer, nullable = False)

    # def create_db():
    #     with app.app_context():
    #         db.create_all()

## creating the books route 

@app.route("/books")

def books():
    
    books_list = Book.query.all()

    return render_template("books.html", books = books_list)

## Creating the add book route

@app.route("/add_book", methods = ["GET", "POST"])

def add_book():
    
    if request.method == "POST":
        
        title = request.form["title"]

        author = request.form["author"]

        publication_year = request.form["publication_year"]

        new_book = Book(title = title, author=author, publication_year = publication_year)

        db.session.add(new_book)

        db.session.commit()
    
    return render_template("add_book.html")

if __name__== "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)

