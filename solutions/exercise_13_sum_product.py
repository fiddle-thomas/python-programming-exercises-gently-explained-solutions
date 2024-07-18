# Function to calculate the sum of numbers in a list
def calculate_sum(numbers):
    # Return 0 if the list is empty
    if not numbers:
        return 0
    sum_total = 0
    # Iterate through the list and add each number to the sum
    for i in numbers:
        sum_total += i
    return sum_total
    

# Function to calculate the product of numbers in a list
def calculate_product(numbers):
    # Return 1 if the list is empty
    if not numbers:
        return 1
    product = 1
    # Iterate through the list and multiply each number to the product
    for i in numbers:
        product *= i
    return product

# Test cases
assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30
assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840