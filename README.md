# Expense Tracker (A Django Application)

## Description

The **Expense Tracker** is a personal web-based financial management tool built with **Python** and the **Django** framework. It is designed to help users efficiently manage and monitor their personal finances by logging, organizing, and tracking expenses.

**Key Features:**
* **User Authentication:** Secure registration and login functionality using Django's built-in authentication system.
* **Expense Tracking:** Users can record expenses with details like title, amount, date, and notes.
* **Category Management:** Expenses are linked to user-specific categories for easy filtering and organization.
* **Dashboard View:** A centralized dashboard provides quick access to recent expenses and the total amount spent.
* **Responsive Design:** The application is styled with Bootstrap to ensure a user-friendly experience across devices.
* **Monthly Summary:** Users can view a summary of their expenses for the current month.
* **SQLite Database:** Uses SQLite as the default database for development and testing.

***

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Dependencies

First, navigate into the directory (`expense_tracker_project/`) and install the required Python packages using pip:

```
cd expense_tracker_project

pip install -r requirements.txt
```

### Initialize the database

Before running the application, the database must be initialized and a superuser created. Ensure you are in the `expense_tracker_project/` directory where `manage.py` is located.

1. **Create database migrations:** This command generates the SQL entries required by the models in the `expenses` app.

2.  Run the Flask initialization command:

    ```
    python manage.py makemigrations
    ```
3. **Apply migrations to the database:** This command executes the migrations, creating the necessary database tables (and the `db.sqlite3 file`).

   ```
    python manage.py migrate
   ```
4. **Create a Superuser (Administrator):** This command creates the administrator login for your /admin side of the project. Follow the prompts to set a username, email, and password.

   ```
    python manage.py createsuperuser
   ```

### Program Execution

Once the database is initialized, you can start the development server

1. **Run the Django Development Server:** Ensure you are in the expense_tracker_project/ directory.

    ```
    python manage.py runserver
    ```

2. **Access the Application:** 
   1. Open your web browser and navigate to the local server address: `http://127.0.0.1:8000/`
   2. To access the admin dashboard: `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created earlier.

You can now register a new user or log in with your superuser credentials to begin tracking your expenses.

 
***

## Authors

Rifat Hossain

***

## Version History

* 0.1
    * Initial Release

***

## Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/en/5.2/)
* [Django Tutorial](https://www.w3schools.com/django/index.php)
* [Bootstrap 5 (CSS framework for styling)](https://getbootstrap.com/)
* [SQLite (Database)](https://www.sqlite.org/index.html)
* [ChatGPT](https://chatgpt.com/g/g-p-69188a96679c81919ff2e35f0072dc-django-project/project)
