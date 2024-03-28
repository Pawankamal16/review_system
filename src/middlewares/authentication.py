# authentication.py

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

jwt = JWTManager()

@jwt_required()
def validate_token():
    # Validate JWT token
    current_user_id = get_jwt_identity()
    if current_user_id:
        return current_user_id
    else:
        return {"error": "Invalid token"}, 401
