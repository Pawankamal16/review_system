# review_routes.py

from flask import Blueprint, request
from controller.review_controller import submit_review
from middleware.authentication import validate_token

review_bp = Blueprint('review', __name__)

@review_bp.route('/events/<int:event_id>/reviews', methods=['POST'])
def submit_event_review(event_id):
    data = request.get_json()
    user_id = validate_token()
    return submit_review(user_id, event_id, **data)
