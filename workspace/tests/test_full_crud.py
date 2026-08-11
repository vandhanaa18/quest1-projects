"""Complete Test Implementation - All Expense Tracker Functional Tests."""


import unittest, sys as s, os.path as p, shutil, sqlite3
from datetime import timedelta


class TestCaseForCRUDOperations(unittest.TestCase):
    """Test all CRUD operations: add_expense/remove_category_name/display_all_transactions etc. plus edge cases like duplicate categories validation, date range filtering tests and category management functionality."""

    
    @classmethod def setUpClass(cls) -> None: 
        # Initialize test database (SQLite in-memory for isolation between runs or temporary file-based db):
        
