from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from utils.db_mongo import mongo_db
from bson import ObjectId

members_bp = Blueprint('members', __name__)

@members_bp.route('/members', methods=['GET'])
def list_members():
    members = list(mongo_db.members.find())
    return render_template('members/list.html', members=members)

@members_bp.route('/members', methods=['POST'])
def add_member():
    data = request.form.to_dict()
    member_id = mongo_db.members.insert_one(data).inserted_id
    return redirect(url_for('members.list_members'))

@members_bp.route('/members/<id>', methods=['GET'])
def get_member(id):
    member = mongo_db.members.find_one({'_id': ObjectId(id)})
    return render_template('members/detail.html', member=member)

@members_bp.route('/members/<id>', methods=['POST'])
def update_member(id):
    data = request.form.to_dict()
    mongo_db.members.update_one({'_id': ObjectId(id)}, {'$set': data})
    return redirect(url_for('members.get_member', id=id))

@members_bp.route('/members/delete/<id>', methods=['POST'])
def delete_member(id):
    mongo_db.members.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('members.list_members'))
