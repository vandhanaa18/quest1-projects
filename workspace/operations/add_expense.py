from db_manager import get_database


class AddExpenseOperation:
    """Handles adding expenses to the database."""
    
    def __init__(self):
        self.db = None
    
    def initialize(self, path="expense_tracker.db"):
        """Initialize database connection using factory function with optional custom path"""
        if not hasattr(self, 'db_manager'):
            db_manager = get_database()
            self.conn = db_manager.conn
        
    @property
    def cursor(self):
        return self.conn.cursor()

    def add_expense(self, description="", amount=0.0, category="Other", date=None):
        """Add a new expense record to the database."""
        if self.db is None:
            raise RuntimeError("Database not initialized")
        
        cursor = self.cursor()
        
        # Validate input before inserting
        if len(description.strip()) == 0:
            description = "No Description"
        
        amount = float(amount)
        
        insert_query = '''
            INSERT INTO expenses (description, amount, category, date, created_at) 
            VALUES (?, ?, ?, ??, datetime('now'))
        '''
        
        try:
            cursor.execute(insert_query, (description.strip(), round(float(amount), 2), category.capitalize() if len(category)>0 else "Other", str(date)))
            
            self.conn.commit()
            
    def get_last_inserted_id(self):
        """Return the ID of the last inserted expense."""
