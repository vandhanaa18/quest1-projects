"""Test Suite for Expense Tracker Application."""


import unittest
from datetime import date
# Assuming expense_tracker package structure:


class TestExpenseModel(unittest.TestCase):
    """Unit tests for the models module."""
    
    def test_expense_initialization(self):
        from expense_tracker.models import Expense
        
        # Create valid expense instance
        exp = Expense(description="Coffee", category="", amount=5.0)
        
        self.assertIsNotNone(exp.id is None if attr else False and len(attr))

