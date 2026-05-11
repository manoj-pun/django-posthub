# PostHub - Django Practice Project
A simple social media-style application built with Django to practice CRUD operations, user authentication, file uploads, and template inheritance using PostgreSQL database.

## Purpose
This project was created for learning Django fundamentals including:
- User authentication (login/register/logout)
- Creating, reading, updating, and deleting posts (CRUD)
- File/image uploads with Pillow
- PostgreSQL database configuration
- Environment variables for security
- User profiles and relationships

## What the Application Does
- Users can register and create accounts
- Upload posts with images and descriptions
- View posts on a feed/homepage
- View other users' profiles
- Update or delete their own posts
- Edit their profile information and picture

## How to Run on Your Computer

### Prerequisites
- Python 3.8+ installed
- PostgreSQL installed and running

### Step-by-Step Setup

1. **Clone the project to your desktop**
   ```bash
   git clone https://github.com/manoj-pun/django-posthub.git
   cd django-posthub

2. **Create a virtual environment within that folder**
   ```bash
   python -m venv .venv

3. **Activate the virtual environment**
   ```bash
    # On Windows:
    venv\Scripts\activate

    # On Mac/Linux:
    source .venv/bin/activate

4. **Install dependencies**
   ```bash
    pip3 install -r requirements.txt

5. **Set up PostgreSQL Database**

    First, create a database in PostgreSQL:
   
    Open PostgreSQL command line or pgAdmin and run these SQL commands:
   ```sql
    CREATE DATABASE yourdatabasename;
    CREATE USER yourusername WITH PASSWORD 'yourpassword';
    ALTER ROLE yourusername SET client_encoding TO 'utf8';
    ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
    ALTER ROLE yourusername SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE posthub_db TO yourusername;

6. **Create Environment Variables file**

   Create a .env file in the root directory (same level as manage.py):
   ```bash
    # PostgreSQL Database settings
    DB_NAME=yourdatabasename
    DB_USER=yourusername
    DB_PASSWORD=yourpassword
    DB_HOST=localhost
    DB_PORT=5432

7. **Run database migrations**
   ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate

8. Create a superuser (admin account)
   ```bash
    python3 manage.py createsuperuser
    # Follow the prompts to create an admin account

9. Start the development server
   ```bash
    python3 manage.py runserver
