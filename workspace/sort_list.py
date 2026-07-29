#!/usr/bin/env python3
"""Python program to sort a list."""


def sort_simple_method():
    """Sorts a list using Python's built-in sorted() function (returns new list)."""
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Create and print original list
    original_list = numbers.copy()
    print("Original List:", original_list)
    
    # Sort using sorted() - returns a new sorted list
    sorted_numbers = sorted(original_list)
    print("\nSorted List (using sorted()):", sorted_numbers)


def sort_inplace_method():
    """Sorts a list in-place using the .sort() method."""
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original List:", numbers)
    
    # Sort in-place - modifies original list directly
    numbers.sort(reverse=True)  # reverse=False for ascending order
    print("\nSorted List In-Place (descending):", numbers)


def sort_custom_key():
    """Sorts a list with custom key function."""
    people = [
        ("Alice", 30),
        ("Bob", 25),
        ("Charlie", 35),
        ("Diana", 28)
    ]
    
    # Sort by age (second element of tuple) in ascending order
    sorted_people = sorted(people, key=lambda x: x[1])
    print("People sorted by age:")
    for name, age in sorted_people:
        print(f" {name} - Age: {age}")


def sort_strings():
    """Sorts a list of strings alphabetically."""
    words = ["banana", "Apple", "cherry", "date"]
    
    # Default case-insensitive sorting (Python uses Unicode values)
    sorted_words = sorted(words, key=str.lower)
    print("Original Words:", words)
    print("\nSorted Words (case-insensitive):", sorted_words)


def sort_nested_list():
    """Sorts a list of dictionaries by specific keys."""
    products = [
        {"name": "Laptop", "price": 1200, "stock": 5},
        {"name": "Phone", "price": 800, "stock": 10},
        {"name": "Tablet", "price": 400, "stock": 3}
    ]
    
    # Sort by price in ascending order
    sorted_products = sorted(products, key=lambda x: x["price"])
    print("Products sorted by price (ascending):")
    for product in sorted_products:
        print(f" {product['name']} - ${product['price']}, Stock: {product['stock']}")


def main():
    """Main function to demonstrate various sorting methods."""
    print("=" * 50)
    print("Python List Sorting Examples".center(50))
    print("=" * 50 + "\n")
    
    # Example 1: Simple built-in sort (returns new list)
    print("\n--- Method 1: Using sorted() function ---")
    sort_simple_method()
    
    # Example 2: In-place sorting with .sort() method
    print("\n" + "-" * 50)
    sort_inplace_method()
    
    # Example 3: Sorting custom data structures (by key)
    print("\n" + "-" * 50)
    sort_custom_key()
    
    # Example 4: String sorting
    print("\n" + "-" * 50)
    sort_strings()
    
    # Example 5: Nested list/dictionary sorting
    print("\n" + "-" * 50)
    sort_nested_list()


if __name__ == "__main__":
    main()
