import os

class Config:
    MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/library')
    NEO4J_URI = os.environ.get('NEO4J_URI', 'bolt://localhost:7687')
    NEO4J_USER = os.environ.get('NEO4J_USER', 'neo4j')
    NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD', 'password')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
