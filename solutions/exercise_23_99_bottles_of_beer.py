# Loop from 99 to 1, representing the bottles of beer
for previous_stock in range(99, 0, -1):
    # Calculate the number of bottles after taking one down
    current_stock = previous_stock - 1

    # Handle singular/plural cases and the "No more bottles" case
    if current_stock == 1:
        previous_inventory = f"{previous_stock} bottles"
        current_inventory = f"{current_stock} bottle"
    elif current_stock == 0:
        previous_inventory = f"{previous_stock} bottle"
        current_inventory = "No more bottles"
    else:
        previous_inventory = f"{previous_stock} bottles"
        current_inventory = f"{current_stock} bottles"
    
    # Print the first part of the stanza      
    print(f"{previous_inventory} of beer on the wall,")
    print(f"{previous_inventory} of beer,")
    print(f"Take one down,")      
    print(f"Pass it around,")
    
    # Handle the last line differently for the final case
    if current_stock == 0:
        print(f"{current_inventory} of beer on the wall!")
    else:
        print(f"{current_inventory} of beer on the wall,\n")