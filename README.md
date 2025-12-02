# 🚀 Wagtail CMS – Local Setup & Development Guide

This project utilizes a source build of Wagtail for maximum flexibility, alongside custom StreamField blocks and Tailwind CSS for modern front-end development.

Follow the steps below to set up the environment, install dependencies, build the Wagtail admin interface, and run the project locally.

---

## 1. Get the Code

### 1.1 Clone the Repository

```bash
git clone <YOUR_REPO_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 1.2 Clone Wagtail Source

Since this project uses a source build of Wagtail, you'll need to clone the Wagtail repository into your project directory.

```bash
git clone https://github.com/wagtail/wagtail.git
```

This will create a `wagtail/` directory within your project containing the Wagtail source code.

---

## 2. Python Environment Setup

### 2.1 Create & Activate Virtual Environment (venv)

It is highly recommended to isolate your dependencies using a virtual environment.

```bash
# Create the environment
python3 -m venv venv

# Activate on macOS & Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 2.2 Install Python Requirements

This project uses `pyproject.toml` for dependency management (Poetry/Hatch style), but standard pip installation is also supported.

```bash
# Recommended: If using Poetry (or similar tool)
poetry install

# Alternative: If using pip/setuptools with pyproject.toml
pip install -e .
```

**Optional Legacy Step:** To generate a `requirements.txt` file for sharing or deployment:

```bash
pip freeze > requirements.txt
```

---

## 3. Frontend & Wagtail Admin Build

Since this project uses a Wagtail source build, you must build the necessary static assets for the admin interface.

### 3.1 Install Node Dependencies

Navigate into the Wagtail source directory and install Node dependencies.

```bash
cd wagtail
npm install
```

### 3.2 Build Admin Assets

Run the build script to generate the admin CSS and JavaScript files.

```bash
npm run build
```

This command populates `wagtail/admin/static/wagtailadmin/` with the required files.

---

## 4. Database & Static Files

### 4.1 Collect Static Files

Return to the main project directory (where `manage.py` is located) and collect all static assets.

```bash
cd ..  # Go back to the root project folder
python manage.py collectstatic
```

### 4.2 Apply Database Migrations

Set up the necessary database schema for Django and Wagtail.

```bash
python manage.py migrate
```

### 4.3 Create Admin User

Create a superuser to access the Wagtail admin interface.

```bash
python manage.py createsuperuser
```

---

## 5. Running the Application

### 5.1 Start the Server

```bash
python manage.py runserver
```

### Access Points

| Interface | Address |
|-----------|---------|
| Frontend Site | http://127.0.0.1:8000 |
| Wagtail Admin | http://127.0.0.1:8000/admin |

---

## 6. Project Structure

A schematic view of the core directories:

```
project/
├── mysite/                 # Main Django project settings
├── cms_app/                # Your custom CMS application (models, blocks, templates)
├── wagtail/                # Wagtail source repo
├── venv/                   # Virtual environment
├── pyproject.toml          # Python dependency file
└── manage.py
```

### Custom Blocks & Templates Location

| Content Type | Filepath | Purpose |
|--------------|----------|---------|
| Page Models | `cms_app/models.py` | Defines StreamFields and Page structures. |
| Block Templates | `cms_app/templates/cms_app/blocks/` | HTML rendering for individual StreamField blocks. |
| Static Assets | `cms_app/static/cms_app/` | CSS, JS, and images specific to your app. |

---


## Prototype Images

Here are some sample images used in this project:

![Image 1](Images(prototype)/image-1.png)
![Image 2](Images(prototype)/image-2.png)
![Image 7](Images(prototype)/Image-7.png)
![Image 4](Images(prototype)/Image-4.png)
![Image 5](Images(prototype)/image-5.png)
![Image 6](Images(prototype)/image-6.png)

