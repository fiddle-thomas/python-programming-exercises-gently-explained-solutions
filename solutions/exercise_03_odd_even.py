# Function to check if a number is odd
def is_odd(number):
    return number % 2 == 1

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Test cases to verify the correctness of the is_odd function
assert is_odd(42) == False
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False # Floats should not be considered odd

# Test cases to verify the correctness of the is_even function
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False # Floats should not be considered even