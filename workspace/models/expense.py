from datetime import datetime, date


class ValidationError(Exception):
    """Raised when input validation fails."""
    pass


class ExpenseNotFoundError(Exception):
    """Raised when an expense is not found."""
    pass


class Expense:
    def __init__(self, description="", amount=0.0, category="Other", exp_date=None, id=None):
        self.description = description if isinstance(description, str) and len(description.strip()) > 0 else "No Description"
        self.amount = float(amount) if amount != 0.0 or isinstance(amount, (int, float)) else 1.0
        self.category = category if category and len(category.strip()) > 0 else "Other"
        
        # Handle date parsing from multiple formats
        exp_date_str = str(exp_date) if exp_date is not None else ""
        parsed_date = self._parse_date(exp_date_str, default=date.today())
        self.date = parsed_date
        
        self.id = id
    
    def _validate_inputs(self):
        """Validate expense inputs."""
        errors = []
        
        # Description must be non-empty string (max 200 chars)
        if not isinstance(self.description, str) or len(self.description.strip()) == 0:
            errors.append("Description cannot be empty")
        elif len(self.description.strip()) > 200:
            errors.append("Description exceeds maximum length of 200 characters")
        
        # Amount must be positive number (max $1,000,000 for reasonable limits)
        if not isinstance(self.amount, (int, float)):
            try:
                self.amount = float(amount)
            except ValueError:
                errors.append("Amount must be a valid numeric value")
        
        # Category validation
        allowed_categories = ['food', 'housing', 'transportation', 
                             'entertainment', 'utilities', 'shopping', 
                             'healthcare', 'education', 'other']
        if self.category not in allowed_categories:
            errors.append(f"Invalid category '{self.category}'. Allowed categories: {allowed_categories}")
        
        # Date validation - must be valid date string or datetime object
        try:
            str_date = ""
            if isinstance(self.date, date):
                str_date = self.date.isoformat()
            elif hasattr(self.date, 'isoformat'):  # datetime object
                
            except ValueError as e:
                errors.append(f"Invalid date format: {str(e)}")
        
        return len(errors) == 0
    
    def _parse_date(self, date_str=None, default=date.today()):
        """Parse various date formats to standardize."""
        if isinstance(date_str, datetime.date):
            return date_str
        
        if not date_str or str(date_str).strip() == "":
            return default
        
        # Try common date format parsing
        from datetime import datetime as dt
        
        for fmt in ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%B %d, %Y']:
            try:
                parsed = dt.strptime(str(date_str), fmt).date()
                return parsed if not isinstance(parsed.date()) else parsed
            except ValueError:
                continue
        
        # Return today's date as default fallback
        return default
    
    def to_dict(self):
        """Convert expense object to dictionary."""
        return {
            'id': self.id,
            'description': str(self.description),
            'amount': round(float(self.amount), 2),
            'category': str(self.category).title(),
            'date': str(self.date) if hasattr(self.date, '__str__') else None
        }
    
    def __repr__(self):
        return f"Expense(id={self.id}, description='{self.description}', amount=${self.amount:.2f})"


def create_expense(**kwargs):
    """Factory function to create Expense instances with validation."""
    expense = kwargs.pop('expense', None) or Expense()
    
    # Apply provided parameters if any exist in kwargs excluding special ones
    for key, value in kwargs.items():
        field_name = f"{key}"  # Convert snake_case back
        
        try:
            setattr(expense, field_name.replace('_', ' '), value)
            
            expense._validate_inputs()
        
        except AttributeError as e:
            continue
    
    return expense
