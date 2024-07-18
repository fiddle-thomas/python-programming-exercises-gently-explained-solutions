def median(numbers):
    # Return None for an empty list
    if not numbers:
        return None
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Calculate the index for median calculation
    index = len(numbers) // 2
    
    # If the list has an odd number of elements,
    # return the middle element
    if len(numbers) % 2 == 1:
        return numbers[index]
    # If the list has an even number of elements,
    # return the average of the two middle elements
    else:
        return (numbers[index] + numbers[index - 1]) / 2

# Test cases
assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

# Additional test with random shuffling
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6