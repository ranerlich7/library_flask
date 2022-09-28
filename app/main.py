from flask import Flask, redirect, url_for
from app.upload import upload_bp
from app.books import books_bp

UPLOAD_FOLDER = 'uploads'
DOWLOAD_FOLDER = '../uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWLOAD_FOLDER'] = DOWLOAD_FOLDER
app.register_blueprint(upload_bp)
app.register_blueprint(books_bp)

@app.route("/")
def main():
    return redirect(url_for('books.books'))

if __name__ == "__main__":
  app.run(debug=True)