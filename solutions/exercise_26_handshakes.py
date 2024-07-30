# function to count unique handshakes between people from a given list
def print_handshakes(people: list):
    # counts handshakes
    handshakes = 0
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            print(f"{people[i]} shakes hands with {people[j]}")
            handshakes += 1
    return handshakes

if __name__ == "__main__":
    assert print_handshakes(['Alice', 'Bob']) == 1
    assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
    assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
    
