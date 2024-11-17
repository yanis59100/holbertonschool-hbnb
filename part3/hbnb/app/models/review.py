from hbnb.app.models.base_model import BaseModel
from hbnb.app.models.user import User
from hbnb.app.models.place import Place
from hbnb.app import db


class Review(BaseModel):
    __tablename__ = 'reviews'
    __table_args__ = (
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='rating_check'),
    )

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating, user, place):
        super().__init__()
        self.text = self._validate_text(text)
        self.rating = self._validate_rating(rating)
        self.user = self._validate_user(user)
        self.place = self._validate_place(place)

    def _validate_rating(self, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        return rating

    def _validate_user(self, user):
        if not isinstance(user, User):
            raise ValueError("User must be valid instances")
        return user

    def _validate_place(self, place):
        if not isinstance(place, Place):
            raise ValueError("Place must be valid instances")
        return place

    def _validate_text(self, text):
        if not text:
            raise ValueError("Text cannot be empty")
        return text
