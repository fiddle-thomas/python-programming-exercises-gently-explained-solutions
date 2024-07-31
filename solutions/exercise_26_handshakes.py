# Function to print and count unique handshakes between people from a given list
def print_handshakes(people: list):
    # Variable to count handshakes
    handshakes = 0
    
    # Nested loops to iterate through pairs of people
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            # Print the handshake
            print(f"{people[i]} shakes hands with {people[j]}")
            # Increment the handshake count
            handshakes += 1
    
    # Return the total number of handshakes
    return handshakes

# Test cases
if __name__ == "__main__":
    assert print_handshakes(['Alice', 'Bob']) == 1
    assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
    assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6