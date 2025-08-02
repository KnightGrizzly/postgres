from flask import Blueprint, render_template, flash
from src.models.event import Event


events_bp = Blueprint('events', __name__)

@events_bp.route('/events')
def events():
    """Показати всі заходи"""
    try:
        events_list = Event.get_all()
        if events_list is None:
            flash('Помилка підключення до бази даних', 'error')
            events_list = []
        return render_template('events.html', events=events_list)
    except Exception as e:
        flash(f'Помилка: {e}', 'error')
        return render_template('events.html', events=[])