from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['MONGODB_URI'] = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/learning_platform')

# Initialize database
from shared.database.db_init import init_db
init_db(app)

login_manager = LoginManager(app)
login_manager.login_view = 'module1.login'

# Import models after db is initialized
from shared.database import models

# Import module routes
from module1_ui.backend.routes import module1_bp
from module2_user_data.backend.routes import module2_bp
from module3_ai_processing.backend.routes import module3_bp
from module4_voice_visual.backend.routes import module4_bp
from module5_reminders.backend.routes import module5_bp

# Register blueprints
app.register_blueprint(module1_bp)
app.register_blueprint(module2_bp)
app.register_blueprint(module3_bp)
app.register_blueprint(module4_bp)
app.register_blueprint(module5_bp)

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.objects(id=user_id).first()
    except:
        return None


if __name__ == '__main__':
    # Render provides the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    
    # Run the Flask app on the correct host and port
    app.run(host="0.0.0.0", port=port, debug=True)