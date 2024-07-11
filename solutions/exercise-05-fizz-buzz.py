# Function to play the FizzBuzz game up to a specified number
def fizz_buzz(up_to):
    # Iterate over each number from 1 to 'up_to'
    for number in range(1, up_to + 1):
        # Check if the number is divisible by both 3 and 5
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")  # Print "FizzBuzz" if divisible by both
        # Check if the number is divisible by 3
        elif number % 3 == 0:
            print("Fizz", end=" ")  # Print "Fizz" if divisible by 3
        # Check if the number is divisible by 5
        elif number % 5 == 0:
            print("Buzz", end=" ")  # Print "Buzz" if divisible by 5
        # If the number is not divisible by 3 or 5, print the number itself
        else:
            print(number, end=" ")

# Call the function to play FizzBuzz up to 35
fizz_buzz(35)
