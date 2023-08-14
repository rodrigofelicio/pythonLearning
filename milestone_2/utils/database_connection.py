import sqlite3

#Context Manager for database connection
class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host


    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type or exc_val or exc_tb:
            self.connection.commit()
        self.connection.close()