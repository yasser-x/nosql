from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from utils.db_neo4j import neo4j_db

authors_bp = Blueprint('authors', __name__)

@authors_bp.route('/authors', methods=['GET'])
def list_authors():
    query = "MATCH (a:Author) RETURN a"
    authors = neo4j_db.query(query)
    return render_template('authors/list.html', authors=authors)

@authors_bp.route('/authors', methods=['POST'])
def add_author():
    data = request.form.to_dict()
    query = """
    CREATE (a:Author {id: $id, name: $name})
    """
    parameters = {
        'id': data['id'],
        'name': data['name']
    }
    neo4j_db.query(query, parameters)
    return redirect(url_for('authors.list_authors'))

@authors_bp.route('/authors/<id>', methods=['GET'])
def get_author(id):
    query = "MATCH (a:Author {id: $id}) RETURN a"
    parameters = {'id': id}
    author = neo4j_db.query(query, parameters)
    return render_template('authors/detail.html', author=author[0])

@authors_bp.route('/authors/<id>', methods=['POST'])
def update_author(id):
    data = request.form.to_dict()
    query = """
    MATCH (a:Author {id: $id})
    SET a.name = $name
    """
    parameters = {
        'id': id,
        'name': data['name']
    }
    neo4j_db.query(query, parameters)
    return redirect(url_for('authors.get_author', id=id))

@authors_bp.route('/authors/delete/<id>', methods=['POST'])
def delete_author(id):
    query = """
    MATCH (a:Author {id: $id})
    DELETE a
    """
    parameters = {'id': id}
    neo4j_db.query(query, parameters)
    return redirect(url_for('authors.list_authors'))
