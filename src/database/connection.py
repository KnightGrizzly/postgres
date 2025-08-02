import psycopg2
from psycopg2.extras import DictCursor
from src.config import Config


def get_db_connection():
    """
    Функція для підключення до бази даних PostgreSQL

    Returns:
        connection: З'єднання з базою даних або None у разі помилки
    """
    try:
        conn = psycopg2.connect(**Config.DATABASE_CONFIG)
        return conn
    except Exception as e:
        print(f"Помилка підключення до БД: {e}")
        return None


def execute_query(query, params=None, fetch=False):
    """
    Виконує SQL запит до бази даних

    Args:
        query (str): SQL запит
        params (tuple): Параметри для запиту
        fetch (bool): Чи потрібно повернути результат

    Returns:
        list або None: Результат запиту або None у разі помилки
    """
    conn = get_db_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute(query, params)

        if fetch:
            result = cursor.fetchall()
        else:
            result = None

        conn.commit()
        cursor.close()
        conn.close()

        return result

    except Exception as e:
        print(f"Помилка виконання запиту: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return None