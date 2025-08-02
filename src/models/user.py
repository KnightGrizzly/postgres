from src.database.connection import execute_query


class User:
    """Клас для роботи з користувачами"""

    @staticmethod
    def get_all():
        """
        Отримати всіх користувачів

        Returns:
            list: Список користувачів
        """
        query = "SELECT * FROM users ORDER BY id"
        return execute_query(query, fetch=True)

    @staticmethod
    def get_by_id(user_id):
        """
        Отримати користувача за ID

        Args:
            user_id (int): ID користувача

        Returns:
            dict: Дані користувача або None
        """
        query = "SELECT * FROM users WHERE id = %s"
        result = execute_query(query, (user_id,), fetch=True)
        return result[0] if result else None

    @staticmethod
    def create(name, email, phone=None):
        """
        Створити нового користувача

        Args:
            name (str): Ім'я користувача
            email (str): Email користувача
            phone (str): Телефон користувача

        Returns:
            bool: True якщо успішно створено
        """
        query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
        result = execute_query(query, (name, email, phone))
        return result is not None

    @staticmethod
    def update(user_id, name, email, phone=None):
        """
        Оновити дані користувача

        Args:
            user_id (int): ID користувача
            name (str): Нове ім'я
            email (str): Новий email
            phone (str): Новий телефон

        Returns:
            bool: True якщо успішно оновлено
        """
        query = "UPDATE users SET name = %s, email = %s, phone = %s WHERE id = %s"
        result = execute_query(query, (name, email, phone, user_id))
        return result is not None

    @staticmethod
    def delete(user_id):
        """
        Видалити користувача

        Args:
            user_id (int): ID користувача

        Returns:
            bool: True якщо успішно видалено
        """
        query = "DELETE FROM users WHERE id = %s"
        result = execute_query(query, (user_id,))
        return result is not None