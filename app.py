from flask import Flask
from config import Config
from blueprints.books.routes import books_bp
from blueprints.authors.routes import authors_bp
from blueprints.members.routes import members_bp
from blueprints.loans.routes import loans_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(authors_bp, url_prefix='/authors')
app.register_blueprint(members_bp, url_prefix='/members')
app.register_blueprint(loans_bp, url_prefix='/loans')

if __name__ == '__main__':
    app.run(debug=True)

