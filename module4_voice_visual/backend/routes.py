from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from shared.database.models import Topic

module4_bp = Blueprint('module4', __name__)

@module4_bp.route('/text-to-speech/<topic_id>')
@login_required
def text_to_speech(topic_id):
    topic = Topic.objects(id=topic_id).first()
    if not topic:
        flash('Topic not found')
        return redirect(url_for('module1.dashboard'))
    if topic.user_id != str(current_user.id):
        flash('Access denied')
        return redirect(url_for('module1.dashboard'))
    return render_template('module4_voice_visual/frontend/audio_player.html', topic=topic)

@module4_bp.route('/api/synthesize/<topic_id>')
@login_required
def synthesize_speech(topic_id):
    topic = Topic.objects(id=topic_id).first()
    if not topic:
        return jsonify({'error': 'Topic not found'}), 404
    if topic.user_id != str(current_user.id):
        return jsonify({'error': 'Access denied'}), 403
    
    return jsonify({
        'text': topic.explanation,
        'topic': topic.topic_name
    })
