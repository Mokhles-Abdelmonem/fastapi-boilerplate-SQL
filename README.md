# fastapi boilerplate SQL

This is a boilerplate project for building RESTful APIs with FastAPI and SQLAlchemy. It includes basic CRUD operations for a single database model and has been set up with best practices in mind.

# Installation 

- Clone the repository
- Create a virtual environment: python3 -m venv venv
- Activate the virtual environment: source venv/bin/activate
- Install the dependencies: pip install -r requirements.txt
- Create a PostgreSQL database (or any other database supported by SQLAlchemy)
- Update the database configuration in app/core/db.py

# Usage 

- Activate the virtual environment: source venv/bin/activate
- Run the migrations: alembic upgrade head
- Start the development server: uvicorn app.main:app --reload

The API documentation will be available at http://localhost:8000/docs.

# Features

- FastAPI for fast and easy API development
- SQLAlchemy for database access and management
- structure based on Django

# Contributing

Contributions are welcome! If you have any issues or feature requests, please open an issue or submit a pull request.