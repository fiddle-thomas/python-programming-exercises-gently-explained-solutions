# Function to print the ASCII table for characters in the range 32 to 126
def print_ascii_table():
    # Loop through numbers from 32 to 126 (inclusive)
    for number in range(32, 127):
        # Print the number and its corresponding ASCII character
        print(number, chr(number))

# Call the function to print the ASCII table
print_ascii_table()
