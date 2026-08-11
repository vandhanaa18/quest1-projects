"""Test Cases for Expense Tracker CRUD Operations - All Scenarios."""


import unittest, os, sys


class TestCRUDOperations(unittest.TestCase):
    """Comprehensive tests covering all Create/Read/Update/Delete scenarios."""

    
    @classmethod def setUpClass(cls) -> None: 
        cls.db_manager = DatabaseManager(':memory:')  # Using in-memory DB for speed
        
        
