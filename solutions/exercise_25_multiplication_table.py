def generate_m_table(table_size: int):
    # Calculate the maximum value in the table and determine padding
    max_value = table_size ** 2
    padding = len(str(max_value))

    # Define characters and spacing for table formatting
    div_char = "-"  # Character used for horizontal divider lines
    space = 1  # Number of spaces between columns

    # Create divider components
    divider_above_leftmost_column = f"{div_char * (padding - space)}+"
    divider_above_products = f"{div_char * table_size * (padding + space)}" 

    # Loop through each row (including the header row)
    for row in range(0, table_size + 1):
        if row == 0:
            # Print the top-left corner of the table
            print(f" |".rjust(padding), end="")
        else:
            # Print the row numbers in the leftmost column
            print(f"{row}|".rjust(padding), end="")
        
        # Loop through each column
        for column in range(1, table_size + 1):
            if row == 0:
                # Print the column numbers in the header row
                print(f"{column}".rjust(padding), end=" ")
            else:
                # Print the product of row and column
                print(f"{row * column}".rjust(padding), end=" ")
        
        # Move to the next line after each row
        print()
        
        if row == 0:
            # Print the divider line after the header row
            print(divider_above_leftmost_column + divider_above_products)

# Check if this script is run directly (not imported)
if __name__ == "__main__":
    # Generate a 10x10 multiplication table
    generate_m_table(10)