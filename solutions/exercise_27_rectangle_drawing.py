def draw_rectangle(width: int, height: int):
    # Check if both width and height are positive
    if width > 0 and height > 0:
        # Iterate over the number of rows
        for _ in range(height):
            # Print a row of '#' characters
            # Use string multiplication to create the row
            print("#" * width)

# Example usage
if __name__ == "__main__":
    draw_rectangle(10, 4)