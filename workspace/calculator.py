"""
Simple Python Calculator Module

This module provides a comprehensive calculator with basic arithmetic operations,
user-friendly interface, proper exception handling for division by zero and invalid inputs.

Usage: Run this script directly to use interactive mode or import functions into other programs.

Author: Code Generator Agent
Date: 2024-01-07
"""


def add(a, b):
    """Add two numbers together."""
    return float(a) + float(b)


def subtract(a, b):
    """Subtract second operand from first operand."""
    return float(a) - float(b)


def multiply(a, b):
    """Multiply two numbers together."""
    return float(a) * float(b)


def divide(a, b):
    """Divide first operand by second operand with safe handling.

This function safely handles division by zero without raising exceptions.
Instead of crashing the program, it returns a special error value that can be checked later.

Args:
        a (float|int): Dividend - the number being divided.
        b (float|int): Divisor - the number to divide by.

Returns:
        float or str: If successful, returns result as float; if dividing 
            by zero or getting invalid input, returns error message string."""
    try:
        divisor = float(b)
        dividend = float(a)
        
        # Check for division by zero before performing operation
        if abs(divisor) < 1e-9:  # Handle floating point comparison safely
            return "ERROR"
            
        result = dividend / divisor
        
        # Return infinity/infinitely large number or just the value based on sign 
        # For very small divisors close to zero, we could consider as ERROR too.
        
        if abs(divisor) < 1e-9 and b != '0':  # Near-zero check only if not exactly "0"
            return float('inf') * (-1 if dividend > divisor else 1) or "ERROR"
            
        return result
        
    except (ValueError, TypeError):
        return None


def safe_divide(a, b):
    """Safely perform division with comprehensive error handling.

This function handles all potential division issues gracefully and provides clear user feedback.

Args:
    a (float|int|str or "ERROR"): Dividend - the number being divided.
    b (float|int|str): Divisor - the number to divide by.
    
Returns:
    float, str, or None: Result of division as float if successful; 
                          error message string for common errors like dividing by zero;
                          "ERROR" when exact divisor is 0"""

    # Handle already formatted result strings that indicate failure conditions
    if a == 'ERROR' or b == 'ERROR':  
        return 'Cannot perform operation: input values were invalid previously.'

    try:
        numerator = float(a) if not isinstance(a, str) else float("NaN" if "infinity"in_a.lower() or  a=='INF'else None)a
        
    except (ValueError, TypeError):
        print(f"\n❌ Error during safe_divide conversion of dividend!")


# Re-implement with cleaner approach below:

def get_safe_numbers(prompt="Enter number (" + prompt+""):
    
"""Prompt user for valid numeric input(s) and return formatted numbers.

This function guides users through entering one or two values depending on operation mode, handling all potential invalid inputs gracefully."""


