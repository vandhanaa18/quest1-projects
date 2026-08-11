"""Database module for Expense Tracker application."""

import sqlite3
from contextlib import contextmanager


class DatabaseManager:
    """Manages SQLite database connections and operations."""
    
    def __init__(self, db_path='expenses.db'):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Context manager for safe database connection handling."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
    
    def create_tables(self):
        """Create necessary tables for expense tracking."""
        with self.get_connection() as cursor:
            # Create expenses table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL CHECK(amount >= 0),
                    date DATE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create categories table for better organization
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    type TEXT CHECK(type IN ('income', 'expense')),
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
    def add_category(self, name: str, category_type: str = None) -> int:
        """Add a new expense/income category."""
        with self.get_connection() as cursor:
            try:
                cursor.execute('''
                    INSERT INTO categories (name, type) 
                    VALUES (?, ?)
                ''', (name.lower(), category_type))
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                # Category already exists - get existing ID instead of raising error
                cursor.execute('SELECT id FROM categories WHERE LOWER(name) = ?', (name.lower(),))
                row = cursor.fetchone()
                if row:
                    return row[0]
        
        with self.get_connection() as cursor:
            try:
                cursor.execute('''
                    INSERT OR IGNORE INTO categories (name, type) 
                    VALUES (?, ?)
                ''', (name.lower(), category_type))
            except sqlite3.IntegrityError:
                pass
            
    def get_all_categories(self):
        """Retrieve all expense/income categories."""
        with self.get_connection() as cursor:
            cursor.execute('SELECT id, name, type FROM categories ORDER BY name')
            return cursor.fetchall()
    
    def add_expense(self, description: str, category_name: str, amount: float, date: str) -> int:
        """Add a new expense record."""
        # Get or create category ID first to ensure consistency
        try:
            cat_id = self._get_or_create_category(category_name.lower(), 'expense')
        except Exception as e:
            raise ValueError(f"Invalid category: {category_name}") from e
        
        with self.get_connection() as cursor:
            cursor.execute('''
                INSERT INTO expenses (description, category, amount, date) 
                VALUES (?, ?, ?, ?)
            ''', (description, cat_id, amount, date))
            
            return cursor.lastrowid
    
    def add_income(self, description: str, category_name: str, amount: float, date: str) -> int:
        """Add a new income record."""
        # Get or create category ID first to ensure consistency
        try:
            cat_id = self._get_or_create_category(category_name.lower(), 'income')
        except Exception as e:
            raise ValueError(f"Invalid category for income: {category_name}") from e
        
        with self.get_connection() as cursor:
            cursor.execute('''
                INSERT INTO expenses (description, category, amount, date) 
                VALUES (?, ?, ?, ?)
            ''', (description, cat_id, amount, 'income'))
            
            return cursor.lastrowid
    
    def _get_or_create_category(self, name: str, default_type: str):
        """Helper to get existing or create new category."""
        with self.get_connection() as cursor:
            # Try to find existing category
            cursor.execute('SELECT id FROM categories WHERE LOWER(name) = ?', (name.lower(),))
            
            result = cursor.fetchone()
            if result is not None and len(result) > 0:
                return int(result[0])
            
            # Create new category with default type or keep as 'expense' for backwards compatibility
            try:
                cursor.execute('INSERT OR REPLACE INTO categories (name, type) VALUES (?, ?)', 
                             (name.lower(), self._infer_type(name)))
                cursor.lastrowid = None  # Reset lastrowid since we're not using it directly here
            except sqlite3.IntegrityError as e:
                raise ValueError(f"Invalid category name: {name}") from e
        
        with self.get_connection() as cursor:
            try:
                cursor.execute('SELECT id FROM categories WHERE LOWER(name) = ?', (name.lower(),))
                result = cursor.fetchone()
                if result is not None and len(result) > 0:
                    return int(result[0])
                
                # This should have been created by previous statement, but in case of any error
                raise ValueError(f"Failed to create category: {name}") from e
        
    def _infer_type(self, name: str):
        """Infer category type based on common expense/income keywords."""
        if name.lower() in ['salary', 'income', 'bonus', 'investment']:
            return 'income'
        
        # Default to income for categories that sound like money coming in
        elif any(keyword in name.lower() and not 
                keyword.startswith('credit') and not 
                keyword.endswith(('fee', 'tax'))) or \
             any(income_keyword in name.lower() for income_keyword in ['paycheck', 'wage', 'revenue']):
            return 'income'
        
        # Default to expense - common keywords for expenses
        if any(expense_keyword in name.lower() for expense_keyword in [
                'food', 'grocery', 'transportation', 'entertainment', 
                'utilities', 'rent', 'shopping', 'dining']) or \
             any(keyword.endswith(('fee', 'tax')) for keyword in name.split()):
            return 'expense'
        
        # Default to income if ambiguous (safer default)
        return None
    
    def get_expenses_by_date_range(self, start_date: str = None, end_date: str = None):
        """Retrieve expenses within a date range."""
        with self.get_connection() as cursor:
            query = 'SELECT id, description, category, amount FROM expenses WHERE 1=1'
            
            if start_date is not None and end_date is not None:
                try:
                    parsed_start = _parse_date(start_date)
                    parsed_end = _parse_date(end_date)
                    
                    # Add appropriate date filters based on format
                    query += ' AND (date >= ? OR (? IS NULL))'
                    cursor.execute(query, [start_date if not start_date else f"{start_date}", 
                                           end_date])
                except Exception as e:
                    raise ValueError("Invalid date formats. Use YYYY-MM-DD") from e
                    
            elif start_date is None and end_date is None:
                query += ''  # Return all expenses
                
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_expenses_by_category(self, category_name: str):
        """Retrieve expenses by category."""
        with self.get_connection() as cursor:
            cursor.execute('''
                SELECT id, description, category, amount FROM expenses 
                WHERE LOWER(category) LIKE ?
            ''', (category_name.lower(), '%'))
            
            return cursor.fetchall()
    
    def get_total_by_category(self):
        """Get total amounts grouped by category."""
        with self.get_connection() as cursor:
            cursor.execute('''
                SELECT category, SUM(amount), COUNT(*) 
                FROM expenses 
                GROUP BY category
                ORDER BY amount DESC
            ''')
            
            return cursor.fetchall()
    
    def get_all_expenses(self):
        """Retrieve all expense records."""
        with self.get_connection() as cursor:
            query = 'SELECT id, description, category, amount, date FROM expenses ORDER BY date'
            cursor.execute(query)
            return cursor.fetchall()
    
    def delete_expense(self, expense_id: int):
        """Delete an expense record by ID."""
        with self.get_connection() as cursor:
            cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))


def _parse_date(date_string: str) -> tuple:
    """Parse and validate date string for SQLite comparison."""
    import datetime
    
    try:
        # Try ISO format first
        parsed_start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date() if 'start' in dir().lower()[0] else None
        
except ValueError:
    
def _parse_safe_dates(): pass

