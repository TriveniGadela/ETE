from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from shared.database.models import User, Topic

module2_bp = Blueprint('module2', __name__)

@module2_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        academic_level = request.form.get('academic_level')
        current_user.academic_level = academic_level
        current_user.save()
        flash('Profile updated successfully')
        return redirect(url_for('module2.profile'))
    return render_template('module2_user_data/frontend/profile.html')

@module2_bp.route('/topic-history')
@login_required
def topic_history():
    topics = Topic.objects(user_id=str(current_user.id)).order_by('-created_at')
    return render_template('module2_user_data/frontend/topic_history_new.html', topics=topics)

@module2_bp.route('/topic/<topic_id>')
@login_required
def view_topic(topic_id):
    topic = Topic.objects(id=topic_id).first()
    if not topic:
        flash('Topic not found')
        return redirect(url_for('module2.topic_history'))
    if topic.user_id != str(current_user.id):
        flash('Access denied')
        return redirect(url_for('module2.topic_history'))
    return render_template('module2_user_data/frontend/view_topic.html', topic=topic)
