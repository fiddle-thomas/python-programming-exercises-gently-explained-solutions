# Function to determine the color of a chessboard square based on its row and column
def get_chess_square_color(row, column):
    # Check if the row and column are within the valid range (0-7)
    if row <= 7 and column <= 7:
        # Special case: the square at (0, 0) is white
        if row == 0 and column == 0:
            return "white"
        # For other squares: if the sum of row and column is even, the square is white
        elif (row + column) % 2 == 0:
            return "white"
        # If the sum of row and column is odd, the square is black
        elif (row + column) % 2 == 1:
            return "black"
    else:
        # If the row or column is out of the valid range, return an empty string
        return ""

# Test cases to verify the function works correctly
assert get_chess_square_color(0, 0) == 'white'
assert get_chess_square_color(1, 0) == 'black'
assert get_chess_square_color(0, 1) == 'black'
assert get_chess_square_color(7, 7) == 'white'
assert get_chess_square_color(0, 8) == ''
assert get_chess_square_color(2, 9) == ''