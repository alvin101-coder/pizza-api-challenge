from server.app import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    @validates('price')
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")
        return price

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "restaurant": {"id": self.restaurant.id, "name": self.restaurant.name, "address": self.restaurant.address},
            "pizza": {"id": self.pizza.id, "name": self.pizza.name, "ingredients": self.pizza.ingredients}
        }