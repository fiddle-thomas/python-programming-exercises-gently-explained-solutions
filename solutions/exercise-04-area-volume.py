# Function to calculate the area of a rectangle
def area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def perimeter(length, width):
    return (length * 2) + (width * 2)

# Function to calculate the volume of a rectangular prism
def volume(length, width, height):
    return length * width * height

# Function to calculate the surface area of a rectangular prism
def surface_area(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

# Test cases to verify the correctness of the area function
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40

# Test cases to verify the correctness of the perimeter function
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26

# Test cases to verify the correctness of the volume function
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400

# Test cases to verify the correctness of the surface area function
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340