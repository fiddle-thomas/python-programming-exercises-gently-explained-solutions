# Function to write text to a file, overwriting any existing content
def write_to_file(file, text):
    with open(file, "w") as temp_file:
        temp_file.write(text)

# Function to append text to a file without overwriting existing content
def append_to_file(file, text):
    with open(file, "a") as temp_file:
        temp_file.write(text)

# Function to read the entire content of a file and return it
def read_from_file(file):
    with open(file, "r") as temp_file:
        return temp_file.read()

# Write 'Hello!\n' to 'greet.txt', overwriting any existing content
write_to_file('greet.txt', 'Hello!\n')

# Append 'Goodbye!\n' to 'greet.txt'
append_to_file('greet.txt', 'Goodbye!\n')

# Assert that the content of 'greet.txt' is 'Hello!\nGoodbye!\n'
assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'
