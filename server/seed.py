from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

db.create_all()


restaurants = [
    Restaurant(name="Mario's Pizza", address="Street 123"),
    Restaurant(name="Luigi's Pizza", address="Street 456"),
]

pizzas = [
    Pizza(name="Pepperoni", ingredients="Dough, Tomato, Cheese, Pepperoni"),
    Pizza(name="Veggie", ingredients="Dough, Tomato, Cheese, Bell Peppers, Olives"),
]


db.session.add_all(restaurants + pizzas)
db.session.commit()