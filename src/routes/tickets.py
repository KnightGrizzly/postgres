from flask import Blueprint, render_template, flash
from src.models.ticket import Ticket

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets')
def tickets():
    """Показати всі квитки"""
    try:
        tickets_list = Ticket.get_all()
        if tickets_list is None:
            flash('Помилка підключення до бази даних', 'error')
            tickets_list = []
        return render_template('tickets.html', tickets=tickets_list)
    except Exception as e:
        flash(f'Помилка: {e}', 'error')
        return render_template('tickets.html', tickets=[])