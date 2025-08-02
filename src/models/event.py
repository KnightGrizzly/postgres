from src.database.connection import execute_query


class Event:
    """Клас для роботи з заходами"""

    @staticmethod
    def get_all():
        """
        Отримати всі заходи

        Returns:
            list: Список заходів
        """
        query = "SELECT * FROM events ORDER BY date"
        return execute_query(query, fetch=True)

    @staticmethod
    def get_by_id(event_id):
        """
        Отримати захід за ID

        Args:
            event_id (int): ID заходу

        Returns:
            dict: Дані заходу або None
        """
        query = "SELECT * FROM events WHERE id = %s"
        result = execute_query(query, (event_id,), fetch=True)
        return result[0] if result else None

    @staticmethod
    def create(name, description, date, venue, price, total_tickets=100):
        """
        Створити новий захід

        Args:
            name (str): Назва заходу
            description (str): Опис заходу
            date (str): Дата та час заходу
            venue (str): Місце проведення
            price (float): Ціна квитка
            total_tickets (int): Загальна кількість квитків

        Returns:
            bool: True якщо успішно створено
        """
        query = """
        INSERT INTO events (name, description, date, venue, price, total_tickets) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        result = execute_query(query, (name, description, date, venue, price, total_tickets))
        return result is not None

    @staticmethod
    def update(event_id, name, description, date, venue, price, total_tickets):
        """
        Оновити дані заходу

        Args:
            event_id (int): ID заходу
            name (str): Нова назва
            description (str): Новий опис
            date (str): Нова дата
            venue (str): Нове місце проведення
            price (float): Нова ціна
            total_tickets (int): Нова кількість квитків

        Returns:
            bool: True якщо успішно оновлено
        """
        query = """
        UPDATE events 
        SET name = %s, description = %s, date = %s, venue = %s, price = %s, total_tickets = %s 
        WHERE id = %s
        """
        result = execute_query(query, (name, description, date, venue, price, total_tickets, event_id))
        return result is not None

    @staticmethod
    def delete(event_id):
        """
        Видалити захід

        Args:
            event_id (int): ID заходу

        Returns:
            bool: True якщо успішно видалено
        """
        query = "DELETE FROM events WHERE id = %s"
        result = execute_query(query, (event_id,))
        return result is not None

    @staticmethod
    def get_popular_events():
        """
        Отримати популярні заходи (з більш ніж 2 проданими квитками)

        Returns:
            list: Список популярних заходів
        """
        query = """
        SELECT 
            e.name as "Назва заходу",
            e.venue as "Місце проведення",
            e.date as "Дата заходу",
            e.price as "Ціна квитка",
            COUNT(t.id) as "Кількість проданих квитків"
        FROM events e
        JOIN tickets t ON e.id = t.event_id
        GROUP BY e.id, e.name, e.venue, e.date, e.price
        HAVING COUNT(t.id) > 2
        ORDER BY COUNT(t.id) DESC
        """
        return execute_query(query, fetch=True)