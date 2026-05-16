This is a simple portfolio website created with Django.

## Description

This project is a personal portfolio website. It shows information about me and displays my projects.

The projects can be added through the Django admin page.

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

## Features

- Home page
- About section
- Projects section
- Project images
- GitHub links
- Admin page to add new projects

## How to Run the Project

1. Open the project folder in VS Code.

2. Activate the virtual environment:

```bash
.\venv\Scripts\activate
````

3. Install the requirements:

```bash
pip install django pillow
```

4. Run the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```

6. Open the website in the browser:

```text
http://127.0.0.1:8000/
```

## Admin Page

To access the admin page, open:

```text
http://127.0.0.1:8000/admin/
```

In the admin page, I can add, edit, and delete projects.

## What I Learned

In this project, I learned how to:

* Create a Django project
* Create an app
* Use templates
* Use Bootstrap
* Create a model
* Add data using the admin page
* Display database information on a web page

## Author

Jonathan Almeida

