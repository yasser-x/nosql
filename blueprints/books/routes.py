from flask import Blueprint, request, jsonify, render_template
from utils.db_mongo import mongo_db
from utils.db_neo4j import neo4j_db

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def list_books():
    books = list(mongo_db.books.find())
    return render_template('books/list.html', books=books)

@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book_id = mongo_db.books.insert_one(data).inserted_id
    # Sync with Neo4j
    query = """
    CREATE (b:Book {id: $id, title: $title, author_id: $author_id})
    """
    parameters = {
        'id': str(book_id),
        'title': data['title'],
        'author_id': data['author_id']
    }
    neo4j_db.query(query, parameters)
    return jsonify({'message': 'Book added', 'id': str(book_id)}), 201

@books_bp.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = mongo_db.books.find_one({'_id': ObjectId(id)})
    return render_template('books/detail.html', book=book)

@books_bp.route('/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    mongo_db.books.update_one({'_id': ObjectId(id)}, {'$set': data})
    # Sync with Neo4j
    query = """
    MATCH (b:Book {id: $id})
    SET b.title = $title, b.author_id = $author_id
    """
    parameters = {
        'id': id,
        'title': data['title'],
        'author_id': data['author_id']
    }
    neo4j_db.query(query, parameters)
    return jsonify({'message': 'Book updated'})

@books_bp.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    mongo_db.books.delete_one({'_id': ObjectId(id)})
    # Sync with Neo4j
    query = """
    MATCH (b:Book {id: $id})
    DELETE b
    """
    parameters = {
        'id': id
    }
    neo4j_db.query(query, parameters)
    return jsonify({'message': 'Book deleted'})
