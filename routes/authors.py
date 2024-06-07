from flask import Blueprint, request, jsonify
from models.neo4j_models import Neo4jConnection

authors_blueprint = Blueprint('authors', __name__)

# Exemple de route pour ajouter un auteur
@authors_blueprint.route('/add', methods=['POST'])
def add_author():
    data = request.json
    
    # Ajouter un auteur dans Neo4j
    neo4j_conn = Neo4jConnection()
    neo4j_conn.query("""
    CREATE (a:Auteur {nom: $nom})
    """, parameters=data)
    neo4j_conn.close()

    return jsonify({"message": "Auteur ajouté"})
