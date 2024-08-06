def draw_pyramid(height: int):
    """
    Draw a pyramid of '#' characters with the given height.
    
    Args:
    height (int): The number of rows in the pyramid.
    """
    hash_index = 1
    for space_index in range(height, 0, -1):
        # Print spaces followed by '#' characters
        # The number of spaces decreases while the number of '#' increases
        print(space_index * " " + hash_index * "#")
        hash_index += 2

if __name__ == "__main__":
    draw_pyramid(5)