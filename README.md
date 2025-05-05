# Flask RESTful API Demo

A demonstration of a Flask RESTful API with CRUD operations using best practices and an in-memory database.

## Project Structure

```
flask-restful/
├── app.py                  # Main application entry point
├── requirements.txt        # Project dependencies
├── models/                 # Data models
│   ├── __init__.py
│   └── item_model.py       # Item model with in-memory database
├── resources/              # API resources/endpoints
│   ├── __init__.py
│   └── item.py             # Item resource with CRUD operations
└── tests/                  # Test files
    ├── __init__.py
    └── test_item_api.py    # Tests for the API endpoints
```

## Features

- RESTful API built with Flask and Flask-RESTful
- Complete CRUD operations (Create, Read, Update, Delete)
- In-memory database implementation
- Clean project structure following best practices
- Comprehensive test suite

## API Endpoints

| HTTP Method | Endpoint | Description |
|-------------|----------|-------------|
| GET | /items | Get all items |
| GET | /items/{name} | Get a specific item by name |
| POST | /items/{name} | Create a new item |
| PUT | /items/{name} | Update an existing item or create if it doesn't exist |
| DELETE | /items/{name} | Delete an item |

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask development server:

```
python app.py
```

The API will be available at http://127.0.0.1:5000/

## Running Tests

Execute the test suite:

```
pytest
```

## Example API Usage with Postman

### Create an item
1. Set request type to **POST**
2. URL: `http://127.0.0.1:5000/items/chair`
3. Select **Body** tab
4. Choose **raw** and **JSON** format
5. Enter payload:
   ```json
   {
       "price": 19.99,
       "description": "A great item"
   }
   ```
6. Click **Send**

### Get all items
1. Set request type to **GET**
2. URL: `http://127.0.0.1:5000/items`
3. Click **Send**

### Get a specific item
1. Set request type to **GET**
2. URL: `http://127.0.0.1:5000/items/chair`
3. Click **Send**

### Update an item
1. Set request type to **PUT**
2. URL: `http://127.0.0.1:5000/items/chair`
3. Select **Body** tab
4. Choose **raw** and **JSON** format
5. Enter payload:
   ```json
   {
       "price": 29.99,
       "description": "An updated description"
   }
   ```
6. Click **Send**

### Delete an item
1. Set request type to **DELETE**
2. URL: `http://127.0.0.1:5000/items/chair`
3. Click **Send** 