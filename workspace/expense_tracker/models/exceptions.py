"""Expense Model Class implementing data model with CRUD operations."""


VALID_CATEGORIES = ['Housing', 'Transportation', 'Food', 'Entertainment', 
                    'Utilities', 'Shopping', 'Healthcare', 'Education']


class ExpenseNotFoundError(Exception):
    """Exception raised when an expense is not found in the database."""
    
    def __init__(self, id: int = None, message: str = "Expense not found"):
        self.id = id or -1
        super().__init__(f"{message} (expense_id={self.id})")


class ValidationError(Exception):
    """Exception raised when input data fails validation."""

    
    def __str__(self) -> str:
        return f"ValidationError in field '{getattr(self, 'field', '?')}' for value {repr(getattr(self, 'value', ''))}: {getattr(self, 'message', '')}" if hasattr(self, '__dict__') else "ValidationError occurred."


class DatabaseError(Exception):
    """Exception raised for database operation errors."""

    
    pass  # Custom exception for DB operations


