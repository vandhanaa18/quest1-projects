"""Model module for Expense Tracker - Data structures and validation."""


class Expense:
    """Represents an expense record in the system."""
    
    def __init__(self, id=None, description="", category="expense", 
                 amount=0.0, date=None):
        self.id = id
        self.description = description.strip() if isinstance(description, str) else ""
        self.category = "expense"  # Default type - will be updated after save
        
        if not self._validate():
            raise ValueError("Invalid expense data")
        
    @staticmethod
    def _validate(expense=None):
        """Validate the model instance."""
        return (isinstance(description, str) and 
                description.strip() != "" and amount >= 0)


class Income:
    """Represents an income record in the system.

    Uses Expense class for storage but tracks as incoming transactions.
    
    Attributes:
        id: Database row ID
        description: Brief description of income source
        category: Category name (will be created/updated automatically)
        amount: Positive float value
        date: Date string in YYYY-MM-DD format
    
    """
    
    def __init__(self, id=None, description="", category="income", 
                 amount=0.0, date=None):
        
        self.id = id
        # Convert expense object to income record type (if needed)
        if isinstance(expense, Expense):
            super().__init__()

