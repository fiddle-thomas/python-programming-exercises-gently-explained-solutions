def average(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    
    # Initialize sum with the first number
    sum_total = numbers[0]
    
    # Add the rest of the numbers to the sum
    for i in numbers[1:]:
        sum_total += i
    
    # Calculate the total number of elements
    total_numbers = len(numbers)
    
    # Handle the case where all numbers are zero
    if sum_total == 0:
        return 0
    else:
        # Calculate and return the average
        return sum_total / total_numbers

# Test cases
assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

# Additional test with random shuffling
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2