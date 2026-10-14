# Mini Project 5 – IT Help Desk Ticket Management System

**Student:** Adeola Ajayi  
**Course:** INF601 – Advanced Programming in Python  
**Project:** Mini Project 5

## Project Overview

This project is a web-based IT Help Desk Ticket Management System developed using Python, Flask, SQLite, HTML, and Bootstrap.

The application allows users to register, log in securely, create IT support tickets, view their submitted tickets, and update ticket statuses.

## Features

- User registration and login
- Secure password hashing using Werkzeug
- User authentication and session management
- Create IT support tickets
- Assign ticket priorities: Low, Medium, and High
- View submitted support tickets
- Update ticket statuses: Open, In Progress, and Closed
- SQLite database for storing users and tickets
- Responsive user interface using Bootstrap

## Technologies Used

- Python 3.13
- Flask 3.1.3
- SQLite
- HTML and Jinja2
- Bootstrap 5.3.3
- Werkzeug

## Installation Instructions

1. Clone the repository and navigate to the project directory.

2. Create a Python virtual environment:

   `python3 -m venv .venv`

3. Activate the virtual environment on macOS or Linux:

   `source .venv/bin/activate`

4. Install the required dependencies:

   `python -m pip install -r requirements.txt`

5. Initialize the SQLite database:

   `python -m flask --app helpdesk init-db`

6. Start the Flask application:

   `python -m flask --app helpdesk run --debug --port 5001`

7. Open the application in a browser:

   `http://127.0.0.1:5001`

## How to Use the Application

1. Register a new user account.
2. Log in using the registered credentials.
3. Navigate to the support ticket dashboard.
4. Create a new ticket by entering its title, description, and priority.
5. View the submitted ticket on the dashboard.
6. Update its status to Open, In Progress, or Closed.
7. Log out when finished.

## Screenshots

Screenshots demonstrating the application are available in the `screenshots/` directory.

- Initial homepage
- Bootstrap homepage
- User registration
- Successful login
- Support ticket dashboard
- Create support ticket form
- Successful ticket creation
- Successful ticket status update

## Testing

The application was manually tested locally to verify user authentication, ticket creation, dashboard display, and ticket status updates.

Python source files were also checked for syntax errors using:

`python -m compileall -q helpdesk`

## Security Features

- Passwords are stored using secure password hashing rather than plaintext.
- SQL queries use parameterized statements.
- Authentication is required to access support ticket functionality.
- Ticket queries and status updates are restricted to the authenticated user's tickets.

## Author

Adeola Ajayi  
INF601 – Advanced Programming in Python  
Mini Project 5


## AI Usage

ChatGPT was used as an AI assistant during the development of Mini Project 5, an IT Help Desk Ticket Management System built using Python, Flask, SQLite, HTML, and Bootstrap.

**How AI was used:**

AI assisted with generating and explaining Python code for Flask application setup, user authentication, database operations, ticket creation, and ticket status management. It also provided guidance on HTML templates, Bootstrap styling, debugging, Git commands, and README documentation.

**Changes I made to AI-generated code:**

I reviewed and manually modified portions of the AI-generated Python and HTML code to fit my IT Help Desk application. I integrated the authentication and ticket management components, customized the application's interface and ticket management features, and adjusted the Flask development server to use port 5001 because port 5000 was unavailable. I tested the changes locally to verify that the application worked correctly.

**Parts I completed myself:**

I created the project directory structure, configured the Python virtual environment, installed the required dependencies, and initialized the SQLite database. I also manually edited portions of the application code, ran and tested the Flask application, registered a test user, created support tickets, tested ticket status updates, captured screenshots, and managed Git commits.

AI-generated suggestions were reviewed and tested during development. The final application was implemented and verified in my local development environment.
