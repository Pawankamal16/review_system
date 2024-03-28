//review_controller.py

from models.review import Review
from models.user import User

def submit_review(user_id, event_id, registration_exp, event_exp, breakfast_exp, overall_rating):
    //Check if user is authorized to submit a review
    if not User.is_authorized(user_id):
        return {"error": "User is not authorized to submit a review"}, 401
    
    //Create a new review
    review = Review(user_id=user_id, event_id=event_id,
                    registration_experience=registration_exp,
                    event_experience=event_exp,
                    breakfast_experience=breakfast_exp,
                    overall_rating=overall_rating)
    review.save()
    return {"message": "Review submitted successfully"}, 201
