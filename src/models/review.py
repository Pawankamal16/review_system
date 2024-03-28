# review.py

from sqlalchemy import Column, Integer, ForeignKey, Boolean
from database import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    registration_experience = Column(Integer)
    event_experience = Column(Integer)
    breakfast_experience = Column(Integer)
    overall_rating = Column(Integer)
    flagged = Column(Boolean, default=False)
