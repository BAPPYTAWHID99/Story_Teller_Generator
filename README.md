# Story Teller Generator

## Overview
Story Teller Generator is a Django-based application that transforms user-selected creative parameters into a complete, original story. It demonstrates Python, Django, database integration, form validation, API integration, JavaScript, and responsive web design in a single assignment-ready project.

## Features
- Genre, character, location, theme, mood, and length-based story generation
- Validation for required fields and input safety
- Dynamic title generation
- Procedural narrative engine with a structured story arc
- Inspirational quote integration via public API with graceful fallback
- SQLite-backed story persistence and history
- Story read, delete, regenerate, copy, and print actions
- Responsive design and polished storytelling-inspired UI

## Technology Stack
- Python 3.x
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- requests

## System Architecture
- Django Views
- Forms / Validation
- Story Generation Service
- Story Data Layer
- Database
- Public Quote API Integration

## Project Structure
- `story_teller/` — Django project configuration
- `stories/` — app logic, models, forms, views, templates, services, and static files
- `db.sqlite3` — local database
- `requirements.txt` — Python dependencies

## Installation

```bash
git clone <repository-url>
cd story_teller
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Application
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000/

## API Integration
The application requests a public quote from `https://api.quotable.io/random` with a timeout. If the API is unavailable or returns invalid data, the generator still functions and the quote area simply hides or displays a fallback message.

## Testing
```bash
python manage.py test
```

## Screenshots
Add screenshots here after running the application locally.

## Future Improvements
- User accounts and personal story libraries
- AI-powered story variation engine
- Export for PDF or DOCX
- Multi-language story generation

## License
This project is for educational and assignment use.
