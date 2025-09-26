


A comprehensive product inventory management system built with FastAPI backend and React frontend, providing seamless tracking and management of product inventory.

## Features

- **GET /**: Welcome endpoint
- **GET /products/**: Get all products
- **GET /products/?id={id}**: Get a specific product by ID
- **POST /products/**: Create a new product

### Create a new product
```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 5,
       "name": "Monitor",
       "description": "4K monitor",
       "price": 299.99,
       "quantity": 15
     }'
```


## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation
