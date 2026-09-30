from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("hotel.db")
    cursor = connection.cursor()

    # Customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    """)

    # Rooms table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER UNIQUE NOT NULL,
            room_type TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    rooms = [
        (101, "Single", 1500, "Available"),
        (102, "Single", 1500, "Available"),
        (201, "Double", 2500, "Available"),
        (202, "Double", 2500, "Available"),
        (301, "Deluxe", 4000, "Available"),
        (302, "Deluxe", 4000, "Available")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO rooms
        (room_number, room_type, price, status)
        VALUES (?, ?, ?, ?)
    """, rooms)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return render_template("index.html")


# Rooms page
@app.route("/rooms")
def rooms():
    connection = sqlite3.connect("hotel.db")
    connection.row_factory = sqlite3.Row

    rooms = connection.execute(
        "SELECT * FROM rooms"
    ).fetchall()

    connection.close()

    return render_template("rooms.html", rooms=rooms)

@app.route("/customers", methods=["GET", "POST"])
def customers():

    connection = sqlite3.connect("hotel.db")
    connection.row_factory = sqlite3.Row

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]

        connection.execute("""
            INSERT INTO customers
            (name, phone, email, address)
            VALUES (?, ?, ?, ?)
        """, (name, phone, email, address))

        connection.commit()

    customers = connection.execute(
        "SELECT * FROM customers"
    ).fetchall()

    connection.close()

    return render_template(
        "customers.html",
        customers=customers
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)