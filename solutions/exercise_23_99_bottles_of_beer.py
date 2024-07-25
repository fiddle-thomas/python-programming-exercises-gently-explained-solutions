# Print the first verse outside the loop
print("99 bottles of beer on the wall,")
print("99 bottles of beer,")

# Loop from 98 to 0, representing the decreasing number of bottles
for num in range(98, -1, -1):
    # Determine the correct phrase based on the number of bottles
    if num > 1:
        stock = f"{num} bottles"
    elif num == 1:
        stock = f"{num} bottle"
    else:
        stock = "No more bottles"

    # Print the middle part of each verse
    print("Take one down,")      
    print("Pass it around,")

    # Break the loop after printing the last "Take one down, Pass it around"
    if num == 0:
        break
    
    # Print the end of the current verse and the start of the next
    print(f"{stock} of beer on the wall,")
    print(f"\n{stock} of beer on the wall,")
    print(f"{stock} of beer,")

# Print the final line
print(f"{stock} of beer on the wall!")