try:
    import fastapi
    import uvicorn
    import sqlalchemy
    import pydantic
    import jinja2
    import openai
    import dotenv
    import requests
    import gunicorn
    import alembic
    print("All packages are installed correctly.")
except ImportError as e:
    print(f"Error: {e}")
