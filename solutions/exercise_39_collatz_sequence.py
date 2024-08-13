def collatz(starting_number):
    if starting_number % 2 == 0:
        return starting_number // 2
    else:
        return 3 * starting_number + 1

try:
    num = int(input("Enter starting_number: "))
except ValueError:
    print("You must enter an integer.")
else:
    print(num)
    while num != 1:
        num = collatz(num)
        print(num)