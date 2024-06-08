from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from utils.db_mongo import mongo_db
from bson import ObjectId

loans_bp = Blueprint('loans', __name__)

@loans_bp.route('/loans', methods=['GET'])
def list_loans():
    loans = list(mongo_db.loans.find())
    return render_template('loans/list.html', loans=loans)

@loans_bp.route('/loans', methods=['POST'])
def add_loan():
    data = request.form.to_dict()
    loan_id = mongo_db.loans.insert_one(data).inserted_id
    return redirect(url_for('loans.list_loans'))

@loans_bp.route('/loans/<id>', methods=['GET'])
def get_loan(id):
    loan = mongo_db.loans.find_one({'_id': ObjectId(id)})
    return render_template('loans/detail.html', loan=loan)

@loans_bp.route('/loans/<id>', methods=['POST'])
def update_loan(id):
    data = request.form.to_dict()
    mongo_db.loans.update_one({'_id': ObjectId(id)}, {'$set': data})
    return redirect(url_for('loans.get_loan', id=id))

@loans_bp.route('/loans/delete/<id>', methods=['POST'])
def delete_loan(id):
    mongo_db.loans.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('loans.list_loans'))
