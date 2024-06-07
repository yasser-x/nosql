from flask import Blueprint, request, jsonify
from models.mongo_models import adherents

members_blueprint = Blueprint('members', __name__)

# Exemple de route pour ajouter un adhérent
@members_blueprint.route('/add', methods=['POST'])
def add_member():
    data = request.json
    adherent_id = adherents.insert_one(data).inserted_id
    return jsonify({"message": "Adhérent ajouté", "id": str(adherent_id)})
