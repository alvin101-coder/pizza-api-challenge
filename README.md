Pizza API Challenge

This project is a Flask-based API for managing pizzas, restaurants, and their relationships. It supports CRUD operations, validation rules, and data persistence using SQLite.  

### Quick Start

1. Clone the repository:  
   `bash
   git clone https://github.com/alvin101-coder/pizza-api-challenge
   cd pizza-api-challenge  
   `  
2. Install dependencies:  
   `bash
   pipenv install  
   `  
3. Activate the virtual environment:  
   `bash
   pipenv shell  
   `  
4. Run the Flask server:  
   `bash
   flask run  
   `  
By default, the app runs on http://127.0.0.1:5000/.  

---

### Database Setup & Migration

Command Description
flask db init Initialize migrations
flask db migrate -m "Initial migration" Generate migration scripts
flask db upgrade Apply migrations
python server/seed.py Populate the database with sample data

---

### API Routes

Method Endpoint Description
GET /restaurants Fetch all restaurants
GET /restaurants/<id> Fetch a specific restaurant and its pizzas
DELETE /restaurants/<id> Delete a restaurant (cascading delete)
GET /pizzas Fetch all pizzas
POST /restaurant_pizzas Add a pizza to a restaurant

---

### Example Requests & Responses

Fetch All Restaurants
Request:  
`bash
GET /restaurants  
`  
Response:  
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

### Add a Restaurant-Pizza Relationship
Request:  
`bash
POST /restaurant_pizzas  
Content-Type: application/json  
`  
Payload:  
`json
{
  "price": 20,
  "pizza_id": 1,
  "restaurant_id": 2
}
`
Response:  
`json
{
  "id": 1,
  "price": 20,
  "pizza_id": 1,
  "restaurant_id": 2
}
`

---

### Validation Rules

Rule Description
Price Must be between 1 and 30
Error Handling If outside the range, the API returns 400 Bad Request

Example of validation failure response:  
`json
{
  "errors": ["Price must be between 1 and 30"]
}
`

---

Error Handling

Status Code Reason
400 Bad Request Invalid input or validation failure
404 Not Found Resource does not exist
405 Method Not Allowed Incorrect HTTP method used
500 Internal Server Error Unexpected server failure

---

### Postman Instructions

1. Open Postman  
2. Create a New Collection  
3. Add Requests (GET, POST, DELETE)  
4. Set Headers if necessary:  
   - Content-Type: application/json  
5. Test API calls and observe responses  

---

### Contributing

If you would like to contribute:  

1. Fork the repository  
2. Create a feature branch (git checkout -b feature-name)  
3. Commit changes (git commit -m "feat: Add new feature")  
4. Push and create a pull request  

---