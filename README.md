# AI-Powered Learning Platform

A modular, intelligent learning system that simplifies academic topics based on student academic level using OpenAI API.

## 🏗️ Project Structure

```
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
│
├── module1_ui/                     # Module 1: User Interface
│   ├── frontend/
│   │   ├── base.html              # Base template
│   │   ├── home.html              # Landing page
│   │   ├── login.html             # Login page
│   │   ├── register.html          # Registration page
│   │   └── dashboard.html         # User dashboard
│   └── backend/
│       └── routes.py              # UI routes & navigation
│
├── module2_user_data/             # Module 2: User Data & Topics
│   ├── frontend/
│   │   ├── profile.html           # User profile page
│   │   ├── topic_history.html     # Topic history
│   │   └── view_topic.html        # Individual topic view
│   └── backend/
│       └── routes.py              # User & topic management
│
├── module3_ai_processing/         # Module 3: AI Text Processing
│   ├── frontend/
│   │   └── explanation.html       # AI explanation display
│   └── backend/
│       └── routes.py              # AI generation routes
│
├── module4_voice_visual/          # Module 4: Voice & Visual Learning
│   ├── frontend/
│   │   └── audio_player.html      # Text-to-speech player
│   └── backend/
│       └── routes.py              # Audio/visual routes
│
├── module5_reminders/             # Module 5: Reminders & Notifications
│   ├── frontend/
│   │   └── reminders.html         # Reminder management
│   └── backend/
│       └── routes.py              # Reminder CRUD operations
│
└── shared/                        # Shared utilities
    ├── database/
    │   └── models.py              # SQLAlchemy models
    └── utils/
        ├── openai_client.py       # OpenAI API integration
        └── scheduler.py           # Reminder scheduler
```

## 🚀 Features

### Module 1: User Interface
- Home page with platform overview
- User authentication (login/register)
- Dashboard with quick access to features
- Responsive navigation

### Module 2: User Data & Topic Management
- User profile management
- Academic level selection (Elementary to Graduate)
- Topic history tracking
- CRUD operations for user data

### Module 3: AI Text Processing
- OpenAI API integration for AI explanations
- Personalized content based on academic level
- Prompt engineering for different education levels
- Response formatting and storage

### Module 4: Voice & Visual Learning
- Text-to-speech using Web Speech API
- Audio playback controls
- Visual content placeholders
- Multi-modal learning support

### Module 5: Reminders & Notifications
- Create learning reminders
- Schedule notifications
- Background job processing
- Reminder status tracking

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- MongoDB (optional, defaults to local instance)

## 🔧 Installation

1. **Clone or navigate to the project directory:**
```bash
cd c:\Users\anilk\OneDrive\Desktop\hanu
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**
```bash
copy .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini
MONGODB_URI=mongodb://localhost:27017/learning_platform
```

4. **Run the application:**
```bash
python app.py
```

5. **Access the platform:**
Open your browser and navigate to `http://localhost:5000`

## 🎓 Academic Levels

The platform supports 5 academic levels:
- **Elementary School**: Simple language, fun examples
- **Middle School**: Clear language, relatable examples
- **High School**: Key concepts, technical details
- **Undergraduate**: Detailed concepts, theories, applications
- **Graduate**: Advanced concepts, research perspectives

## 🤖 OpenAI Integration

The platform uses OpenAI API for AI-powered explanations:

1. **Model**: GPT-4o-mini (configurable)
2. **Prompt Engineering**: Level-specific prompts
3. **Error Handling**: Comprehensive error messages for API issues

To enable OpenAI:
- Get an API key from OpenAI
- Add the key to your `.env` file
- Ensure you have sufficient credits in your OpenAI account

## 🗄️ Database Schema

### User Table
- id, username, email, password_hash
- academic_level, created_at

### Topic Table
- id, user_id, topic_name
- explanation, academic_level, created_at

### Reminder Table
- id, user_id, message
- scheduled_time, is_sent, created_at

## 🛠️ Technology Stack

- **Backend**: Flask, MongoEngine, Flask-Login
- **Frontend**: HTML, CSS, JavaScript, Jinja2
- **Database**: MongoDB
- **AI**: OpenAI API (GPT-4o-mini)
- **Scheduler**: APScheduler
- **TTS**: Web Speech API

## 📦 Modular Architecture

Each module is self-contained with:
- Separate frontend and backend folders
- Independent routes (Flask Blueprints)
- Clear separation of concerns
- Easy to maintain and scale

## 🔐 Security Features

- Password hashing (Werkzeug)
- Session management (Flask-Login)
- User authentication required for protected routes
- CSRF protection (Flask built-in)

## 🚧 Future Enhancements

- Email notifications for reminders
- Advanced OpenAI models integration
- Image generation for visual learning
- Quiz generation based on topics
- Progress tracking and analytics
- Mobile responsive design improvements

## 📝 License

This project is for educational purposes.

## 👥 Support

For issues or questions, refer to the module-specific documentation in each folder.
