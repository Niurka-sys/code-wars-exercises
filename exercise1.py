
"""Create a function that takes an integer
as an argument and returns "Even" for even numbers or "Odd" for odd numbers."""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"  # return "Odd" if the number is not even
    
# Test cases to validate the function     
print(even_or_odd(2))  # Even           
print(even_or_odd(3))  # Odd

# Output    
# Even
# Odd
"""18 de enero de 2025"""