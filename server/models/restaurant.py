from server.app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', cascade='all, delete-orphan', backref='restaurant')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        }
