# event_routes.py

from flask import Blueprint, request
from controller.event_controller import get_event_summary, get_event_ratings
from middleware.authentication import validate_token

event_bp = Blueprint('event', __name__)

@event_bp.route('/events/<int:event_id>/summary', methods=['GET'])
def event_summary(event_id):
    return get_event_summary(event_id)

@event_bp.route('/events/<int:event_id>/ratings', methods=['GET'])
def event_ratings(event_id):
    return get_event_ratings(event_id)
