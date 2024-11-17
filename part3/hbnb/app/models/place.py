from hbnb.app.models.base_model import BaseModel
from hbnb.app.models.user import User
from hbnb.app import db

class Place(BaseModel):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, title, description, price, latitude, longitude, owner, amenities=[]):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.set_owner(owner)  # Ensure this is a valid User instance
        self.amenities = amenities  # List of Amenity objects
    def validate_title(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        if len(title) > 100:
            raise ValueError("Title must be less than 100 characters")
        return title

    def validate_price(self, price):
        if price < 0:
            raise ValueError("Price must be a non-negative value")
        return price

    def validate_latitude(self, latitude):
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        return latitude

    def validate_longitude(self, longitude):
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        return longitude

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def set_owner(self, owner):
        """Set the owner of the place."""
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")
        return owner

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
