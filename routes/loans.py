from flask import Blueprint, request, jsonify
from models.mongo_models import prets

loans_blueprint = Blueprint('loans', __name__)

# Exemple de route pour emprunter un livre
@loans_blueprint.route('/borrow', methods=['POST'])
def borrow_book():
    data = request.json
    pret_id = prets.insert_one(data).inserted_id
    return jsonify({"message": "Livre emprunté", "id": str(pret_id)})
