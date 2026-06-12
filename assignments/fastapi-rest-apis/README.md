# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework. Students will create endpoints for managing a simple items collection, handle data validation, and test the API with sample requests.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI app with a main application file and define routes for listing, retrieving, creating, and deleting items.

#### Requirements
Completed program should:

- Create a FastAPI application in `main.py`
- Define a root endpoint at `/` that returns a welcome message
- Define an endpoint at `/items` that returns a list of all items
- Define an endpoint at `/items/{item_id}` that returns a single item by ID

### 🛠️ Add Item Creation and Deletion Endpoints

#### Description
Add endpoints that let users create new items and delete existing items, using Pydantic models for validation.

#### Requirements
Completed program should:

- Define a Pydantic model named `Item` with `id`, `name`, `description`, and `price` fields
- Add a POST endpoint at `/items` that accepts an `Item` payload and returns the created item
- Add a DELETE endpoint at `/items/{item_id}` that removes the item and returns a success message
- Use an in-memory list to store items for the application runtime

### 🛠️ Validate Requests and Handle Errors

#### Description
Implement request validation and graceful error handling for invalid or missing resources.

#### Requirements
Completed program should:

- Return a `422` error when the request payload is invalid
- Return a `404` error with a helpful message when an item is not found
- Use Pydantic validation for the request body
- Include example sample requests in the README
