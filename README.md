# Hotel Management System

A basic Hotel Management System website made using Python, Flask, SQLite, HTML and CSS.

The project is designed to manage basic hotel information such as rooms and customer details through a simple web interface.

## Features

The current version of the project includes:

* Hotel home page
* Room management and room details
* Display of available rooms
* Customer registration
* Customer information stored in a database
* SQLite database
* Simple and clean web interface
* CSS styling for the website

## Technologies Used

* **Python** – Main programming language
* **Flask** – Used to create the web application
* **SQLite** – Used to store hotel and customer data
* **HTML** – Used to create the web pages
* **CSS** – Used for styling the website

## Project Structure

```text
Hotel Management/
│
├── app.py
├── hotel.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── rooms.html
│   └── customers.html
│
├── static/
│   └── css/
│       └── style.css
│
└── venv/
```

## Requirements

Before running the project, make sure the following are installed:

* Python 3.10 or above
* VS Code or any other Python editor
* A web browser such as Chrome or Edge

SQLite does not need to be installed separately because Python provides SQLite support through its built-in `sqlite3` module.

## How to Set Up the Project

### 1. Download or clone the project

Download the project from GitHub or copy the project folder to your computer.

Open the project folder in VS Code.

The main folder should contain:

```text
app.py
requirements.txt
templates
static
```

### 2. Open the terminal

In VS Code, open:

**Terminal → New Terminal**

Make sure the terminal is opened inside the project folder.

For example:

```text
C:\Users\YourName\Hotel Management>
```

### 3. Create a virtual environment

Run:

```bash
python -m venv venv
```

This creates a separate Python environment for the project.

The project folder will now contain:

```text
venv/
```

### 4. Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\activate
```

If PowerShell does not allow the activation script, the project can still be run using the Python executable inside the virtual environment.

For example:

```powershell
.\venv\Scripts\python.exe app.py
```

### 5. Install the required packages

Make sure `requirements.txt` contains:

```text
Flask
```

Then install Flask using:

```bash
pip install -r requirements.txt
```

If the virtual environment is not activated, you can also use:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 6. Check the project configuration

No additional configuration file or API key is required for the current version.

The application uses SQLite, so the database is stored locally in:

```text
hotel.db
```

The database is created automatically by the Python application if it does not already exist.

The application also creates the required database tables when it starts.

### 7. Run the application

Run:

```bash
python app.py
```

If you are using the virtual environment directly:

```powershell
.\venv\Scripts\python.exe app.py
```

After starting the application, the terminal should show a message similar to:

```text
* Running on http://127.0.0.1:5000
```

### 8. Open the website

Open a web browser and visit:

```text
http://127.0.0.1:5000
```

The Hotel Management System home page should appear.

## Main Pages

### Home Page

The home page provides an introduction to the Hotel Management System and links to the main sections of the website.

### Rooms Page

The Rooms page displays the rooms available in the hotel along with information such as:

* Room number
* Room type
* Price per night
* Room status

The initial room data is added to the SQLite database by the Python program.

### Customer Page

The Customer page is used to register hotel customers.

The user can enter:

* Customer name
* Phone number
* Email
* Address

After registration, the customer information is stored in the SQLite database and can be displayed on the page.

##
