
from flask import Flask, jsonify

print("NAME :" , __name__)

app = Flask(__name__)

print(app)

@app.route("/")
def hello():
    x = 2+2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    return  "About me"  

@app.route("/books")
@app.route("/books.json")
def list_books():
    books =[
        {"id": 1, "title": "Book1"},
        {"id": 2, "title": "Book2"},
        {"id": 3, "title": "Book3"}
    ]
    return  jsonify(books)      