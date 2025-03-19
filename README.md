# Laboratory-1

Laboratory 1 : Introduction to Django

## Description

This repository shows the steps to follow to create a project using Django.

### Previus Requeriments

-   Python >= 3.7
-   Any text editor

### How to create a project

Follow these steps to create a project using Django:

1.  **Create main project directory**

    ```bash
    mkdir my_django_project
    cd my_django_project
    ```

2.  **Create and activate virtual environment**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    > If `.\venv\Scripts\activate` use this code first `Set-ExecutionPolicy Unrestricted -Scope Process`. This allows the use of scripts in the system.

3.  **Create a source directory**

    ```bash
    mkdir src
    cd src
    ```

4.  **Install Django**

    ```bash
    pip install django
    ```

5.  **Create a project**

    ```bash
    django-admin startproject "name of your project" .

    ```

6.  **Execute the server**

    ```bash
    python manage.py runserver

    ```

Once these steps are completed, you can access the application from any browser in this url: `http://127.0.0.1:8000/`.
