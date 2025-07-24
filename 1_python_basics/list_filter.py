# Even Numbers Filter - Optimized for Speed
"""
A script that prompts the user for a list of numbers and filters out only the even integers.
Handles both space and comma-separated input with robust error handling.
"""

def get_numbers():
    """
    Prompts the user to enter numbers and validates the input.
    
    Returns:
        list: A list of floating-point numbers entered by the user
        
    Raises:
        Continues prompting until valid input is provided
    """
    while True:
        try:
            user_input = input("Enter numbers separated by spaces or commas: ").strip()
            
            # Check for empty input
            if not user_input:
                print("Error: Please enter at least one number!")
                continue
            
            # Handle both space and comma separators efficiently
            # Replace commas with spaces, then split on whitespace
            numbers_str = user_input.replace(',', ' ').split()
            
            # Convert string numbers to floats
            numbers = [float(num) for num in numbers_str]
            return numbers
            
        except ValueError:
            print("Error: Please enter valid numbers only!")

def filter_even_numbers(numbers):
    """
    Filters a list of numbers to return only even integers.
    
    Args:
        numbers (list): List of numbers to filter
        
    Returns:
        list: List containing only even integers from the input
        
    Note:
        Uses bitwise AND operation for efficient even number checking.
        Only includes numbers that are whole numbers (integers).
    """
    # Using list comprehension with bitwise AND for O(1) even check
    # int(num) & 1 == 0 checks if the number is even
    # num == int(num) ensures the number is a whole number
    return [num for num in numbers if int(num) & 1 == 0 and num == int(num)]

def main():
    """
    Main function that orchestrates the program flow.
    Gets numbers from user, filters even numbers, and displays results.
    """
    # Get numbers from user input
    numbers = get_numbers()
    
    # Filter to get only even numbers
    even_numbers = filter_even_numbers(numbers)
    
    # Display results
    if even_numbers:
        print("Even numbers:", even_numbers)
    else:
        print("No even numbers found in the list.")

# Entry point - only run main() if script is executed directly
if __name__ == "__main__":
    main()