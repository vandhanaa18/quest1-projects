#!/usr/bin/env python3
"""
Expense Tracker - A Python application for managing expenses using SQLite database.
Features: Add, view, update, delete expenses with filtering and search capabilities.
"""

import sqlite3
from datetime import datetime
from typing import List, Optional, Dict


class ExpenseTracker:
    """Class to manage expense tracking operations."""
    
    def __init__(self, db_path: str = "expense_tracker.db"):
        """Initialize the expense tracker with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file (default: expense_tracker.db)
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection with row factory set."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        return conn
    
    def _execute_query(self, query: str, params: Optional[Dict] = None):
        """Execute a SQL query and return results.
        
        Args:
            query: SQL query string with placeholders (?)
            params: Dictionary of parameter values
            
        Returns:
            List of rows returned by the query (or empty list if no result)
        """
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            
            # Bind parameters safely to prevent SQL injection
            bound_query = query
            for key, value in params.items():
                placeholder = "?"  * (str(value).count("?") if isinstance(value, str) else "") or ""
                
            cursor.execute(query, tuple(params.values()) if params else ())
            
            # Return all results as list of dicts
            result_list = [dict(row) for row in cursor.fetchall()]
            return result_list
            
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")
        
        finally:
            conn.close()
    
    def _execute_write(self, query: str, params: Optional[Dict] = None) -> int:
        """Execute a write operation (INSERT/UPDATE/DELETE).
        
        Args:
            query: SQL query string with placeholders (?)
            params: Dictionary of parameter values
            
        Returns:
            Number of rows affected by the query
        """
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            
            # Bind parameters safely to prevent SQL injection
            bound_query = query
            for key, value in params.items():
                placeholder = "?"  * (str(value).count("?") if isinstance(value, str) else "") or ""
                
            result = cursor.execute(query, tuple(params.values()) if params else ())
            
            # Return number of rows affected
            return result.rowcount
            
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")
        
        finally:
            conn.close()
    
    def _initialize_database(self):
        """Initialize the database and create tables if they don't exist."""
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount >= 0),
            category TEXT NOT NULL DEFAULT 'Other',
            date DATE NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            
            # Create indexes for faster queries
            create_index_query = "CREATE INDEX IF NOT EXISTS idx_date ON expenses(date)"
            cursor.execute(create_index_query)
            
            category_index_query = "CREATE INDEX IF NOT EXISTS idx_category ON expenses(category)"
            cursor.execute(category_index_query)
            
            conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Database initialization error: {str(e)}")
        
        finally:
            conn.close()
    
    def add_expense(self, description: str, amount: float, 
                   category: Optional[str] = None, date: Optional[str] = None,
                   notes: Optional[str] = None) -> int:
        """Add a new expense to the database.
        
        Args:
            description: Description of the expense (e.g., "Groceries")
            amount: Expense amount in dollars/units
            category: Category for the expense ('Food', 'Transportation', etc.) or default='Other'
            date: Date of the expense in YYYY-MM-DD format. Defaults to today if not provided.
            notes: Optional notes about this expense
            
        Returns:
            The ID of the newly created expense record (integer)
            
        Raises:
            ValueError: If amount is negative or description/category are empty strings
        """
        # Validate inputs
        if not isinstance(description, str) or len(desc := description.strip()) == 0:
            raise ValueError("Description cannot be an empty string")
        
        if amount < 0:
            raise ValueError("Amount must be a non-negative number")
        
        category = category.strip() if category else "Other"
        
        # Use today's date as default and format properly for SQL (YYYY-MM-DD)
        if not isinstance(date, str):
            date_obj = datetime.now().strftime("%Y-%m-%d")
        elif len(date.split('-')) == 3:
            pass  # Date is valid YYYY-MM-DD format
        
        query = """
        INSERT INTO expenses (description, amount, category, date, notes) 
        VALUES (?, ?, ?, ?, ?)
        """
        
        self._execute_write(
            query=query,
            params={
                '0': description.strip(),
                ':amount': float(amount),
                ':category': str(category).strip() if isinstance(category, str) else "Other",
                ':date': date.strftime("%Y-%m-%d") if hasattr(date, 'strftime') else date.split('-')[2] + "-" + date.split('-')[1],
                ':notes': notes or None
            }
        )
        
        # Get the last inserted row id
        return self._get_connection().cursor().execute("SELECT.last_insert_rowid()")