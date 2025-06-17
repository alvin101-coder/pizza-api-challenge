 Pizza API Challenge

This project is a Flask-based API for managing pizzas, restaurants, and the relationship between them. It supports CRUD operations, validation rules, and data persistence using SQLite.

Setup Instructions

=> Install Dependencies
Ensure you have pipenv installed, then run:
"pipenv install"

This will install Flask, Flask-Migrate, Flask-SQLAlchemy, and other required packages.

=> Activate Virtual Environment
Before running any commands, activate your environment:
`
 pipenv shell
`

=> Run the Flask App
Start the Flask server using:
`
flask run
`
By default, it runs on http://127.0.0.1:5000/.


###Database Setup & Migration

=> Initialize Migrations
`
flask db init
`
This sets up migration files.

=> Generate Migration Scripts
`
flask db migrate -m "Initial migration"
`

=> Apply Migrations
`
flask db upgrade
`
This creates necessary tables.

=> Seed the Database
`         
python server/seed.py
`
This populates the database with sample data.


###API Routes & Usage

=> Restaurants
Method Endpoint Description
GET /restaurants Fetch all restaurants
GET /restaurants/<id> Fetch a specific restaurant
DELETE /restaurants/<id> Delete a restaurant

=> Pizzas
Method Endpoint Description
GET /pizzas Fetch all pizzas

=> Restaurant-Pizza Relationship
Method Endpoint Description
POST /restaurant_pizzas Add a pizza to a restaurant


###Example Requests & Responses

=> Fetch All Restaurants
Request
`
GET /restaurants
`
Response
`json
[
  {
    "id": 1,
    "name": "Pizza Hut",
    "address": "123 Main Street"
  },
  {
    "id": 2,
    "name": "Domino's",
    "address": "456 Elm Street"
  }
]
`

=> Add a Restaurant-Pizza Relationship
Request
`bash
POST /restaurant_pizzas
Content-Type: application/json
`
Payload
`json
{
  "price": 20,
  "pizza_id": 1,
  "restaurant_id": 2
}
`
Response
`json
{
  "id": 1,
  "price": 20,
  "pizza_id": 1,
  "restaurant_id": 2
}
`


###Validation Rules
- Price validation in RestaurantPizza
  - Must be between 1 and 30
  - If outside range, API returns 400 Bad Request

Example of validation failure:
`json
{
  "error": "Price must be between 1 and 30"
}
`


###Postman Instructions
(1)Open Postman  
(2) Create a New Collection  
(3) Add Requests (GET, POST, DELETE)
(4) Set Headers (If Necessary):  
   - Content-Type: application/json
(5) Test API Calls and Observe Responses  