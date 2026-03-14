from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import mongoengine as db

class User(UserMixin, db.Document):
    username = db.StringField(required=True, unique=True, max_length=80)
    email = db.StringField(required=True, unique=True, max_length=120)
    password_hash = db.StringField(required=True, max_length=200)
    academic_level = db.StringField(default='high_school', max_length=50)
    age = db.IntField(default=18)
    created_at = db.DateTimeField(default=datetime.utcnow)
    
    meta = {'collection': 'users'}
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id)

class Topic(db.Document):
    user_id = db.StringField(required=True)
    topic_name = db.StringField(required=True, max_length=200)
    explanation = db.StringField()
    academic_level = db.StringField(max_length=50)
    created_at = db.DateTimeField(default=datetime.utcnow)
    
    meta = {'collection': 'topics'}

class Reminder(db.Document):
    user_id = db.StringField(required=True)
    message = db.StringField(max_length=500)
    scheduled_time = db.DateTimeField()
    is_sent = db.BooleanField(default=False)
    created_at = db.DateTimeField(default=datetime.utcnow)
    
    meta = {'collection': 'reminders'}
