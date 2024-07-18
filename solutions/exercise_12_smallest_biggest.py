def get_smallest(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    
    # Initialize smallest with the first element of the list
    smallest = numbers[0]
    
    # Iterate through the rest of the list (starting from the second element)
    for num in numbers[1:]:
        # If we find a smaller number, update smallest
        if num < smallest:
            smallest = num
    
    # Return the smallest number found
    return smallest

def get_biggest(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    
    # Initialize biggest with the first element of the list
    biggest = numbers[0]
    
    # Iterate through the rest of the list (starting from the second element)
    for num in numbers[1:]:
        # If we find a bigger number, update biggest
        if num > biggest:
            biggest = num
    
    # Return the biggest number found
    return biggest

# Test assertions
assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28]) == 2
assert get_smallest([1]) == 1
assert get_smallest([]) == None

assert get_biggest([1, 2, 3]) == 3
assert get_biggest([3, 2, 1]) == 3
assert get_biggest([28, 25, 42, 2, 28]) == 42
assert get_biggest([1]) == 1
assert get_biggest([]) == None