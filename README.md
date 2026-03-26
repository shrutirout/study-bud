# StudyBud

StudyBud is a full-stack collaborative web application where students and developers can create topic-based study rooms, have real-time text conversations, follow other users, and explore what others are studying. It is built with Django and is designed to feel like a community space for learners.

---

## Features

- User registration and login with email-based authentication
- Create, edit, and delete study rooms with a topic and description
- Send and delete messages inside any room
- User profiles with bio, avatar upload, and room history
- Browse and filter rooms by topic
- Search rooms by name, topic, or description
- Activity feed showing the latest messages across all rooms
- Participants list showing everyone who has joined a room
- REST API endpoints to access room data externally
- Fully responsive design that works on mobile and desktop

---

## Tech Stack

**Backend**
- Python 3.12
- Django 4.2.7
- Django REST Framework
- Django CORS Headers
- Pillow (image handling)
- SQLite (default database)

**Frontend**
- Django Template Language (HTML5)
- CSS3 with custom design tokens and CSS variables
- Vanilla JavaScript
- Google Fonts (Inter)

---

## Project Structure

```
StudyBud/
├── base/                   # Main Django app
│   ├── api/                # REST API views, serializers, URLs
│   ├── migrations/         # Database migration files
│   ├── templates/base/     # All HTML templates
│   ├── models.py           # User, Room, Topic, Message models
│   ├── views.py            # All view functions
│   ├── forms.py            # Registration, room, and profile forms
│   ├── urls.py             # App-level URL patterns
│   └── admin.py            # Admin panel registration
├── studybud/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                 # CSS, JS, images, icons
├── templates/              # Base template and navbar
├── requirements.txt
└── manage.py
```

---

## Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites

- Python 3.10 or above
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/shrutirout/study-bud.git
cd study-bud
```

**2. Create and activate a virtual environment**

```bash
pip install virtualenv
virtualenv venv
```

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run database migrations**

```bash
python manage.py migrate
```

**5. Start the development server**

```bash
python manage.py runserver
```

Open your browser and go to: `http://127.0.0.1:8000`

---

## API Endpoints

The project includes a basic REST API built with Django REST Framework.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/rooms/` | Returns a list of all rooms |
| GET | `/api/rooms/<id>/` | Returns details of a specific room |

---

## Environment Notes

- `DEBUG = True` by default, suitable for local development only
- The default database is SQLite, stored as `db.sqlite3` in the root directory
- Uploaded avatars are stored in `static/images/`
- CORS is currently open for all origins, fine for development

---

## License

This project is open source and free to use for learning and personal projects.
