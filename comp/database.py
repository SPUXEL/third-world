import sqlite3


with sqlite3.connect('database.db') as database:
    cursor = database.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            user_id INT,
            user_data TEXT
            )
        """
    )

