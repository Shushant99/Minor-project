# Smart Attendance System (Django + Face Recognition)

Smart attendance app that uses webcam-based face recognition to mark students present, with teacher and admin dashboards for manual control and reporting. [web:1][web:3][web:5]

## Features

- Student master data with class mapping.
- Teacher login and dashboard.
- Real-time camera feed to mark present students using facial recognition.
- Remaining students auto-marked absent after session ends.
- Manual attendance editing by teacher/admin.
- Reports per session.

## Installation

1. Prerequisites
Python version (e.g. 3.10)

CMake and Visual Studio Build Tools (for Windows) or conda requirement

Note that dlib and face-recognition are heavy and may need extra steps.​

2. Local setup
### Create virtual environment

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

### Install dependencies (pip)

pip install -r requirements.txt
Or, if recommending conda:

text
conda env create -f environment.yml
conda activate attend-env


3. Database and run steps
text
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
