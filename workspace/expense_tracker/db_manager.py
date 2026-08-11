"""Database Manager for Expense Tracker - Handles SQLite database operations."""

import sqlite3
from contextlib import contextmanager
from typing import Optional


class DatabaseManager:
    """Manages SQLite database connections and provides CRUD schema initialization."""
    
    def __init__(self, db_path: str = "expense_tracker.db"):
        """Initialize the database manager.
        
        Args:
            db_path: Path to the SQLite database file (default: expense_tracker.db)
        """
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Context manager for acquiring and releasing a database connection.
        
        Yields:
            sqlite3.Connection object
            
        Raises:
            sqlite3.Error: If there's an issue connecting to the database
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row  # Enable dict-like access via column names
            yield conn
            conn.commit()
        except sqlite3.Error as e:
            raise DatabaseError(f"Database error: {e}") from e
        finally:
            if 'conn' in locals():
                try:
                    conn.close()
                except Exception:  # pylint: disable=broad-except
                    pass
    
    def initialize_schema(self) -> bool:
        """Initialize the database schema by creating tables.
        
        Returns:
            True if schema was initialized/updated successfully
            
        Creates the expenses table with the following columns:
            - id (INTEGER PRIMARY KEY AUTOINCREMENT)
            - description (TEXT NOT NULL)
            - amount (REAL CHECK(amount > 0))
            - category (TEXT DEFAULT 'Other')
            - date (DATE DEFAULT CURRENT_DATE)
            - created_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Create expenses table if it doesn't exist
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        amount REAL CHECK(amount > 0),
                        category TEXT DEFAULT 'Other',
                        date DATE DEFAULT CURRENT_DATE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """
                
                cursor.execute(create_table_sql)
                conn.commit()
                
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to initialize schema: {e}") from e
        
        return True
    
    def get_last_id(self) -> Optional[int]:
        """Get the last expense ID in the database.
        
        Returns:
            The last inserted id, or None if table is empty
            
        Raises:
            DatabaseError: If there's an issue querying the database
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Try to get max ID from expenses table
                cursor.execute("SELECT COALESCE(MAX(id), 0) FROM expenses")
                return cursor.fetchone()[0] if cursor.rowcount > 0 else None
                
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to retrieve last id: {e}") from e
    
    def verify_table_exists(self) -> bool:
        """Check if the expenses table exists in the database.
        
        Returns:
            True if the table exists, False otherwise
            
        Raises:
            DatabaseError: If there's an issue querying the database
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Check for expenses table in sqlite_master
                cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name=?;", 
                    ("expenses",)
                )
                return cursor.fetchone() is not None
                
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to verify table existence: {e}") from e
    
    def reset_schema(self):
        """Reset the database schema - drops and recreates tables.
        
        Raises:
            DatabaseError: If there's an issue resetting the schema
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Drop table if it exists (for reset)
                drop_sql = "DROP TABLE IF EXISTS expenses"
                cursor.execute(drop_sql)
                
                recreate_table_sql = """
                    CREATE TABLE expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        amount REAL CHECK(amount > 0),
                        category TEXT DEFAULT 'Other',
                        date DATE DEFAULT CURRENT_DATE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """
                cursor.execute(recreate_table_sql)
                
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to reset schema: {e}") from e


class DatabaseError(Exception):
    """Custom exception for database-related errors."""
    
    pass
