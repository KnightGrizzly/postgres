from flask import Blueprint, render_template, flash
from src.models.user import User


users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def users():
    try:
        users_list = User.get_all()
        if users_list is None:
            flash('Помилка підключення до бази даних', 'error')
            users_list = []
        return render_template('users.html', users=users_list)
    except Exception as e:
        flash(f'Помилка: {e}', 'error')
        return render_template('users.html', users=[])