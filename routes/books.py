from flask import Blueprint, request, jsonify
from models.mongo_models import livres
from models.neo4j_models import Neo4jConnection

books_blueprint = Blueprint('books', __name__)

# Exemple de route pour ajouter un livre
@books_blueprint.route('/add', methods=['POST'])
def add_book():
    data = request.json
    livre_id = livres.insert_one(data).inserted_id
    
    # Synchroniser avec Neo4j
    neo4j_conn = Neo4jConnection()
    neo4j_conn.query("""
    CREATE (l:Livre {titre: $titre, auteur: $auteur, isbn: $isbn, annee: $annee})
    """, parameters=data)
    neo4j_conn.close()

    return jsonify({"message": "Livre ajouté", "id": str(livre_id)})
