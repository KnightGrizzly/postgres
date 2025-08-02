from src.database.connection import execute_query


class Ticket:
    """Клас для роботи з квитками"""

    @staticmethod
    def get_all():
        """
        Отримати всі квитки

        Returns:
            list: Список квитків
        """
        query = "SELECT * FROM tickets ORDER BY purchase_date DESC"
        return execute_query(query, fetch=True)

    @staticmethod
    def get_by_id(ticket_id):
        """
        Отримати квиток за ID

        Args:
            ticket_id (int): ID квитка

        Returns:
            dict: Дані квитка або None
        """
        query = "SELECT * FROM tickets WHERE id = %s"
        result = execute_query(query, (ticket_id,), fetch=True)
        return result[0] if result else None

    @staticmethod
    def create(user_id, event_id, price, seat_number=None, status='active'):
        """
        Створити новий квиток

        Args:
            user_id (int): ID користувача
            event_id (int): ID заходу
            price (float): Ціна квитка
            seat_number (str): Номер місця
            status (str): Статус квитка

        Returns:
            bool: True якщо успішно створено
        """
        query = """
        INSERT INTO tickets (user_id, event_id, price, seat_number, status) 
        VALUES (%s, %s, %s, %s, %s)
        """
        result = execute_query(query, (user_id, event_id, price, seat_number, status))
        return result is not None

    @staticmethod
    def update(ticket_id, user_id, event_id, price, seat_number, status):
        """
        Оновити дані квитка

        Args:
            ticket_id (int): ID квитка
            user_id (int): ID користувача
            event_id (int): ID заходу
            price (float): Ціна квитка
            seat_number (str): Номер місця
            status (str): Статус квитка

        Returns:
            bool: True якщо успішно оновлено
        """
        query = """
        UPDATE tickets 
        SET user_id = %s, event_id = %s, price = %s, seat_number = %s, status = %s 
        WHERE id = %s
        """
        result = execute_query(query, (user_id, event_id, price, seat_number, status, ticket_id))
        return result is not None

    @staticmethod
    def delete(ticket_id):
        """
        Видалити квиток

        Args:
            ticket_id (int): ID квитка

        Returns:
            bool: True якщо успішно видалено
        """
        query = "DELETE FROM tickets WHERE id = %s"
        result = execute_query(query, (ticket_id,))
        return result is not None

    @staticmethod
    def get_tickets_with_details():
        """
        Отримати всі квитки з деталями користувачів та заходів

        Returns:
            list: Список квитків з деталями
        """
        query = """
        SELECT 
            t.id as "ID квитка",
            u.name as "Ім'я користувача",
            e.name as "Назва заходу",
            t.price as "Ціна",
            t.seat_number as "Місце",
            t.purchase_date as "Дата покупки"
        FROM tickets t
        JOIN users u ON t.user_id = u.id
        JOIN events e ON t.event_id = e.id
        ORDER BY t.purchase_date DESC
        """
        return execute_query(query, fetch=True)

    @staticmethod
    def get_expensive_tickets():
        """
        Отримати квитки дорожче 500 грн з деталями

        Returns:
            list: Список дорогих квитків
        """
        query = """
        SELECT DISTINCT
            u.name as "Ім'я користувача",
            u.email as "Email",
            u.phone as "Телефон",
            e.name as "Назва заходу",
            t.price as "Ціна квитка",
            t.purchase_date as "Дата покупки"
        FROM users u
        JOIN tickets t ON u.id = t.user_id
        JOIN events e ON t.event_id = e.id
        WHERE t.price > 500
        ORDER BY t.price DESC, u.name
        """
        return execute_query(query, fetch=True)