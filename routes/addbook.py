from flask import Blueprint, request, jsonify, render_template
from flask_pymongo import PyMongo
from app import mongo  # Assuming mongo is defined in your app.py

addbook_bp = Blueprint('addbook', __name__)

@addbook_bp.route('/add_book')
def add_book_form():
    return render_template('add_book.html')

@addbook_bp.route('/addBook', methods=['POST'])
def add_book():
    book_data = request.json
    mongo.db.livres.insert_one(book_data)
    return jsonify({'status': 'Book added successfully'}), 201
