"""Main Application Module - Entry Point for Expense Tracker."""


import os.path as path
from typing import Optional, Dict, List, Tuple

from .database import DatabaseManager
from models import Expense


class ExpenseTracker:
    """Main class providing expense tracking functionality.
    
    Attributes:
        db_path: Path to SQLite database file
    
    Methods:
        add_expense: Record new expense
        remove_category_name: Delete category by name (helper method)
        
        display_all_transactions: Show all expenses/income with categories
        get_balance_summary: Display income vs expenses summary
        
        generate_monthly_report, create_transaction_entry, etc.
    
    """
    
    def __init__(self, db_path='expenses.db'):
        self.db_manager = DatabaseManager(db_path)

