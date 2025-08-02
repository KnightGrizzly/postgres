from src.database.connection import get_db_connection


def init_database():
    """
    Створення таблиць та заповнення тестовими даними

    Returns:
        bool: True якщо успішно, False у разі помилки
    """
    conn = get_db_connection()
    if not conn:
        return False

    try:
        cursor = conn.cursor()

        # Створення таблиці користувачів
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                phone VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Створення таблиці заходів
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id SERIAL PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                description TEXT,
                date TIMESTAMP NOT NULL,
                venue VARCHAR(200),
                price DECIMAL(10,2) NOT NULL,
                total_tickets INTEGER DEFAULT 100,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Створення таблиці квитків
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                price DECIMAL(10,2) NOT NULL,
                purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                seat_number VARCHAR(10),
                status VARCHAR(20) DEFAULT 'active'
            )
        ''')

        # Перевірка чи є дані в таблицях
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]

        if user_count == 0:
            _populate_test_data(cursor)

        conn.commit()
        cursor.close()
        conn.close()
        return True

    except Exception as e:
        print(f"Помилка створення БД: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return False


def _populate_test_data(cursor):
    """Заповнення бази даних тестовими даними"""

    # Заповнення таблиці користувачів
    users_data = [
        ('Іван Петренко', 'ivan@email.com', '+380501234567'),
        ('Марія Коваленко', 'maria@email.com', '+380671234567'),
        ('Олександр Шевченко', 'alex@email.com', '+380931234567'),
        ('Анна Мельник', 'anna@email.com', '+380501234568'),
        ('Петро Іваненко', 'petro@email.com', '+380671234568'),
        ('Ольга Сидоренко', 'olga@email.com', '+380931234568'),
        ('Максим Бондаренко', 'max@email.com', '+380501234569')
    ]

    cursor.executemany(
        "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)",
        users_data
    )

    # Заповнення таблиці заходів
    events_data = [
        ('Концерт Океан Ельзи', 'Великий концерт популярної української групи',
         '2024-09-15 19:00:00', 'Палац Спорту, Київ', 800.00, 500),
        ('Вистава "Гамлет"', 'Класична вистава Шекспіра',
         '2024-09-20 18:30:00', 'Національний театр, Київ', 450.00, 200),
        ('Стендап вечір', 'Вечір гумору з відомими коміками',
         '2024-09-25 20:00:00', 'Квартира 95, Київ', 350.00, 150),
        ('Фестиваль джазу', 'Міжнародний джазовий фестиваль',
         '2024-10-01 17:00:00', 'Будинок художника, Київ', 600.00, 300),
        ('Виставка картин', 'Сучасне мистецтво України',
         '2024-10-05 10:00:00', 'Музей сучасного мистецтва', 200.00, 1000),
        ('Концерт класичної музики', 'Київський симфонічний оркестр',
         '2024-10-10 19:30:00', 'Філармонія, Київ', 550.00, 400)
    ]

    cursor.executemany(
        "INSERT INTO events (name, description, date, venue, price, total_tickets) VALUES (%s, %s, %s, %s, %s, %s)",
        events_data
    )

    # Заповнення таблиці квитків
    tickets_data = [
        (1, 1, 800.00, '2024-08-01 10:30:00', 'A15', 'active'),
        (2, 1, 800.00, '2024-08-01 11:00:00', 'A16', 'active'),
        (3, 2, 450.00, '2024-08-02 14:20:00', 'B10', 'active'),
        (4, 3, 350.00, '2024-08-03 16:45:00', 'C5', 'active'),
        (1, 4, 600.00, '2024-08-04 09:15:00', 'A20', 'active'),
        (5, 1, 800.00, '2024-08-05 12:30:00', 'A17', 'active'),
        (6, 2, 450.00, '2024-08-06 15:45:00', 'B11', 'active'),
        (7, 3, 350.00, '2024-08-07 17:20:00', 'C6', 'active'),
        (2, 4, 600.00, '2024-08-08 11:10:00', 'A21', 'active'),
        (3, 5, 200.00, '2024-08-09 13:25:00', 'D1', 'active'),
        (4, 6, 550.00, '2024-08-10 14:40:00', 'A5', 'active'),
        (5, 1, 800.00, '2024-08-11 16:55:00', 'A18', 'active'),
        (6, 2, 450.00, '2024-08-12 18:10:00', 'B12', 'active'),
        (7, 4, 600.00, '2024-08-13 19:25:00', 'A22', 'active'),
        (1, 6, 550.00, '2024-08-14 20:40:00', 'A6', 'active')
    ]

    cursor.executemany(
        "INSERT INTO tickets (user_id, event_id, price, purchase_date, seat_number, status) VALUES (%s, %s, %s, %s, %s, %s)",
        tickets_data
    )