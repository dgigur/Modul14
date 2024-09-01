import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)
    #for i in range(1, 5):
        #cursor.execute(
            #f"INSERT INTO Products(title, description, price) VALUES('Продукт{i}', 'Описание{i}', '{i * 100}')")
    connection.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)


def is_included(username):
    check_user = cursor.execute("SELECT username FROM Users WHERE username = ?",
                                (username,))
    if check_user.fetchone() is None:
        return False
    return True




def get_all_products():
    cursor.execute("SELECT * FROM Products")
    connection.commit()
    return cursor.fetchall()


def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()

