def draw_border(width: int, height: int):
    # Check if the width or height is less than 2
    # If so, return without drawing anything
    if width < 2 or height < 2:
        return
    
    # Define characters for different parts of the border
    corner = "+"
    horiz_line = "-" * (width - (len(corner) * 2))  # Calculate horizontal line
    vert_line = "|"
    fill = " " * (width - (len(vert_line) * 2))  # Calculate inner space

    # Iterate through each row of the rectangle
    for row in range(height):
        if row == 0 or row == (height - 1):
            # For first and last row, print top/bottom border
            print(f"{corner}{horiz_line}{corner}")
        else:
            # For middle rows, print vertical borders with space between
            print(f"{vert_line}{fill}{vert_line}")

if __name__ == "__main__":    
    # Test the function with given example
    draw_border(16, 4)