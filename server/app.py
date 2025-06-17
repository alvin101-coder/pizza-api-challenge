from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db) 


from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)