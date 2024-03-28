# user_routes.py

from flask import Blueprint, request
from controller.user_controller import authenticate

user_bp = Blueprint('user', __name__)

@user_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return authenticate(username, password)
