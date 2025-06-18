from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context(): 
    restaurants = [
        Restaurant(name="Mario's Pizza", address="Street 123"),
        Restaurant(name="Luigi's Pizza", address="Street 456"),
    ]

    pizzas = [
        Pizza(name="Pepperoni", ingredients="Dough, Tomato, Cheese, Pepperoni"),
        Pizza(name="Veggie", ingredients="Dough, Tomato, Cheese, Bell Peppers, Olives"),
    ]

    print("Adding restaurants...")
    db.session.add_all(restaurants)
    db.session.commit()
    print(" Restaurants added!")

    print("Adding pizzas...")
    db.session.add_all(pizzas)
    db.session.commit()
    print(" Pizzas added!")

    all_pizzas = Pizza.query.all()
    print(f"Database now contains: {all_pizzas}")

    print(" Seeding complete!")