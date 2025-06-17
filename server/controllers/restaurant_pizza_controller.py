from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.app import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get("price")
    
    if price < 1 or price > 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    restaurant_pizza = RestaurantPizza(**data)
    db.session.add(restaurant_pizza)
    db.session.commit()
    return jsonify(restaurant_pizza.to_dict()), 201
