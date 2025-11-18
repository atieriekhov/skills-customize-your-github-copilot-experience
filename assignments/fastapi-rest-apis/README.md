# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn the fundamentals of building modern REST APIs using the FastAPI framework. Create a functional API with multiple endpoints that demonstrates CRUD operations, request/response handling, and best practices for API development.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with proper project structure and create endpoints for managing a collection of items or resources (e.g., books, tasks, products).

#### Requirements
Completed program should:

- Initialize a FastAPI application with a main app instance
- Create at least 3 endpoints following RESTful conventions (GET, POST, PUT/PATCH, DELETE)
- Define proper request and response models using Pydantic
- Include appropriate HTTP status codes for different scenarios

### 🛠️ Implement CRUD Operations

#### Description
Build complete Create, Read, Update, and Delete operations for your resource with proper error handling and validation.

#### Requirements
Completed program should:

- Accept and validate input data using Pydantic models
- Store and retrieve data (using an in-memory list or simple data structure)
- Handle edge cases such as invalid IDs or missing resources
- Return appropriate error messages and HTTP status codes (404, 400, etc.)
- Include input validation and provide meaningful error responses

### 🛠️ Add API Documentation and Testing

#### Description
Leverage FastAPI's built-in documentation features and create test cases to verify your API works correctly.

#### Requirements
Completed program should:

- Include docstrings and type hints for all endpoints
- Access auto-generated API documentation (Swagger UI and/or ReDoc)
- Test all endpoints using FastAPI's TestClient or a tool like curl/Postman
- Verify that all CRUD operations return expected results
- Document any special behaviors or requirements in comments
