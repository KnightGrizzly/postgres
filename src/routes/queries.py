from flask import Blueprint, render_template, flash
from src.models.ticket import Ticket
from src.models.event import Event


queries_bp = Blueprint('queries', __name__)


@queries_bp.route('/query1')
def query1():
    """Запит 1: Вивести всі квитки разом із назвою заходу та іменем користувача"""
    try:
        results = Ticket.get_tickets_with_details()

        if results is None:
            flash('Помилка підключення до бази даних', 'error')
            results = []
            columns = []
        else:
            # Отримання назв колонок з першого результату
            columns = list(results[0].keys()) if results else []

        return render_template('query_result.html',
                               title="Всі квитки з інформацією про користувачів та заходи",
                               data=results,
                               columns=columns)
    except Exception as e:
        flash(f'Помилка виконання запиту: {e}', 'error')
        return render_template('query_result.html', title="Запит 1", data=[], columns=[])


@queries_bp.route('/query2')
def query2():
    """Запит 2: Показати всі заходи, на які продано понад 2 квитків"""
    try:
        results = Event.get_popular_events()

        if results is None:
            flash('Помилка підключення до бази даних', 'error')
            results = []
            columns = []
        else:
            columns = list(results[0].keys()) if results else []

        return render_template('query_result.html',
                               title="Заходи з більш ніж 2 проданими квитками",
                               data=results,
                               columns=columns)
    except Exception as e:
        flash(f'Помилка виконання запиту: {e}', 'error')
        return render_template('query_result.html', title="Запит 2", data=[], columns=[])


@queries_bp.route('/query3')
def query3():
    """Запит 3: Вивести користувачів, які купили квитки дорожче 500 грн"""
    try:
        results = Ticket.get_expensive_tickets()

        if results is None:
            flash('Помилка підключення до бази даних', 'error')
            results = []
            columns = []
        else:
            columns = list(results[0].keys()) if results else []

        return render_template('query_result.html',
                               title="Користувачі, які купили квитки дорожче 500 грн",
                               data=results,
                               columns=columns)
    except Exception as e:
        flash(f'Помилка виконання запиту: {e}', 'error')
        return render_template('query_result.html', title="Запит 3", data=[], columns=[])