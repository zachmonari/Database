import mysql.connector
from mysql.connector import Error
import pandas as pd

class MySQLDatabase:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='mydatabase',
                user='root',
                password='Zachary4637?'  # Replace with your MySQL password
            )


            print("Connected to MySQL database")

        except Error as e:
            print(f"Error: {e}")
            return None

    def read_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")

            users = cursor.fetchall()
            # Convert to pandas DataFrame
            df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age"])
            print("\nAll Users:")
            print(df.to_string(index=False))
            print("")

            return users

        except Error as e:
            print(f"Error reading users: {e}")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")





if __name__ == "__main__":
    db = MySQLDatabase()
    db.read_users()
    db.close_connection()