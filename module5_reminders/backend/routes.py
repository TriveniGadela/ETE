from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from shared.database.models import Reminder
from datetime import datetime

module5_bp = Blueprint('module5', __name__)

@module5_bp.route('/reminders')
@login_required
def reminders():
    user_reminders = Reminder.objects(user_id=str(current_user.id)).order_by('-scheduled_time')
    return render_template('module5_reminders/frontend/reminders.html', reminders=user_reminders)

@module5_bp.route('/add-reminder', methods=['POST'])
@login_required
def add_reminder():
    message = request.form.get('message')
    scheduled_date = request.form.get('scheduled_date')
    scheduled_time = request.form.get('scheduled_time')
    
    if not message or not scheduled_date or not scheduled_time:
        flash('All fields are required')
        return redirect(url_for('module5.reminders'))
    
    scheduled_datetime = datetime.strptime(f"{scheduled_date} {scheduled_time}", "%Y-%m-%d %H:%M")
    
    reminder = Reminder(
        user_id=str(current_user.id),
        message=message,
        scheduled_time=scheduled_datetime
    )
    reminder.save()
    
    flash('Reminder created successfully')
    return redirect(url_for('module5.reminders'))

@module5_bp.route('/delete-reminder/<reminder_id>')
@login_required
def delete_reminder(reminder_id):
    reminder = Reminder.objects(id=reminder_id).first()
    if not reminder:
        flash('Reminder not found')
        return redirect(url_for('module5.reminders'))
    if reminder.user_id != str(current_user.id):
        flash('Access denied')
        return redirect(url_for('module5.reminders'))
    
    reminder.delete()
    flash('Reminder deleted')
    return redirect(url_for('module5.reminders'))
