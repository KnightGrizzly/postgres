import os


class Config:

    # Flask конфігурація
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

    # Конфігурація бази даних PostgreSQL
    DATABASE_CONFIG = {
        'host': os.environ.get('DB_HOST') or 'localhost',
        'database': os.environ.get('DB_NAME') or 'tickets_db',
        'user': os.environ.get('DB_USER') or 'postgres',
        'password': os.environ.get('DB_PASSWORD') or 'your_password',
        'port': os.environ.get('DB_PORT') or '5432'
    }