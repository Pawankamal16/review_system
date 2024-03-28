# user_controller.py

from models.user import User

def authenticate(username, password):
    # Authenticate user
    user = User.authenticate(username, password)
    if user:
        return {"access_token": user.generate_access_token()}, 200
    else:
        return {"error": "Invalid credentials"}, 401
