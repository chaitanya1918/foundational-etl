import sqlite3

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            phone_number TEXT,
            address TEXT,
            signup_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def load_data(records):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    insert_query = """
        INSERT OR IGNORE INTO users
        (user_id, name, email, phone_number, address, signup_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    for r in records:
        cursor.execute(insert_query, (
            r["user_id"],
            r["name"],
            r["email"],
            r["phone_number"],
            r["address"],
            r["signup_date"]
        ))

    conn.commit()
    conn.close()
    print("Data loaded into users.db")
