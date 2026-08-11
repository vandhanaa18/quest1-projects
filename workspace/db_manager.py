import sqlite3
from pathlib import Path


class DatabaseManager:
    """Manages SQLite connection and schema operations."""
    
    DATABASE_PATH = "expense_tracker.db"
    
    def __init__(self, db_path="expense_tracker.db"):
        self.conn = None
    
    def connect(self):
        conn = sqlite3.connect(str(Path(__file__).parent.parent / self.DATABASE_PATH))
        cursor = conn.cursor()
        
        # Create expenses table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL CHECK(amount > 0),
                category TEXT DEFAULT 'Other',
                date DATE DEFAULT CURRENT_DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT
            )
        ''')
        
        conn.commit()
        self.conn = conn
    
    def close(self):
        if self.conn:
            self.conn.close()
    
    @property
    def cursor(self):
        return self.conn.cursor


def get_database():
    """Factory function to create database connection."""
    db_manager = DatabaseManager("expense_tracker.db")
    db_manager.connect()
    return db_manager
