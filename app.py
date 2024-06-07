from flask import Flask
from config import Config
from routes.books import books_blueprint
from routes.authors import authors_blueprint
from routes.members import members_blueprint
from routes.loans import loans_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Enregistrement des blueprints
app.register_blueprint(books_blueprint, url_prefix='/books')
app.register_blueprint(authors_blueprint, url_prefix='/authors')
app.register_blueprint(members_blueprint, url_prefix='/members')
app.register_blueprint(loans_blueprint, url_prefix='/loans')

if __name__ == '__main__':
    app.run(debug=True)
