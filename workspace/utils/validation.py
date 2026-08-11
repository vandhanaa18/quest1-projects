from models.expense import ValidationError as ExpenseValidationError


def validate_positive_number(value, min_value=None, max_value=None):
    """Validate that a value is a positive number within specified bounds."""
    try:
        num = float(value) if not isinstance(value, (int, float)) else float(value)
        
        error_msg = f"Value must be numeric."
        
        # Check min value constraint - allow very small amounts but > 0
        if min_value is not None and num <= min_value:
            raise ExpenseValidationError(error_msg + " Value must be greater than or equal to the minimum.")
        
        elif max_value is not None and num > max_value:
            error_msg = f"Value exceeds maximum allowed amount." 
            raise ExpenseValidationError(error_msg)
        
    except (TypeError, ValueError) as e:
        raise ExpenseValidationError(str(e))


def validate_string(value):
    """Validate that value is a non-empty string within character limits."""
    if not isinstance(value, str):
        raise ExpenseValidationError("Value must be a string.")
    
    if len(value.strip()) == 0:
        raise ExpenseValidationError("String cannot be empty or contain only whitespace.")


def validate_category(category):
    """Validate expense category against allowed list."""
    allowed_categories = ['food', 'housing', 'transportation', 
                         'entertainment', 'utilities', 'shopping', 
                         'healthcare', 'education', 'other']
    
    if not isinstance(category, str) or len(category.strip()) == 0:
        raise ExpenseValidationError("Category must be a non-empty string.")
    
    # Only check case-insensitive match against allowed categories (lowercase converted for comparison)
    category_lower = category.lower().strip()
    if category_lower not in [c.lower() for c in allowed_categories]:
        valid_options = ', '.join(allowed_categories[:5]) + ", etc." 
        raise ExpenseValidationError(f"Invalid category '{category}'. Allowed categories: {valid_options}")


def validate_date(date_value):
    """Validate date value is a proper date or datetime object."""
    from models.expense import ValidationError as ExpErr
    
    # Accepts string, date, or datetime objects - let the model handle parsing