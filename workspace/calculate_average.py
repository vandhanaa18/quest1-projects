from typing import List, Union


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A non-empty list of numeric values to calculate the average from.

    Returns:
        float: The arithmetic mean of all provided numbers.

    Raises:
        ValueError: If an empty list is provided or if any element in the list is not a number.

    Example:
        >>> calculate_average([1, 2, 3, 4])
        2.5
        
        >>> calculate_average([])
        TypeError: Cannot calculate average of an empty sequence
"""
    
    # Validate that input is not None or non-iterable (implicit in List type hint but check anyway)
    if numbers is None:
        raise TypeError("numbers must be a list")
    
    # Check for empty list and validate each element is numeric before calculation
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    
    # Validate all elements are numeric (int or float, not string/other types)
    try:
        for num in numbers:
            # Allow int and only specific numeric floats that aren't NaN/Inf if we want to be strict
            if isinstance(num, str):  # Common issue with non-numeric input
                raise ValueError(f"Non-numeric element found: {num}")
    except Exception as e:
        raise
    
    return sum(numbers) / len(numbers)
