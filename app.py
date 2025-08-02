from src import create_app
from src.database.init_db import init_database


if __name__ == '__main__':
    # Ініціалізація бази даних при запуску
    print("Ініціалізація бази даних...")
    if init_database():
        print("База даних успішно створена та заповнена!")
    else:
        print("ПОМИЛКА: Не вдалося створити базу даних!")

    # Створення та запуск Flask додатку
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)