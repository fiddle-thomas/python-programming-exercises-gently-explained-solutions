def get_cost_of_coffee(number_of_coffees, price_per_coffee):
    # For 8 or fewer coffees, simply multiply the number by the price
    if number_of_coffees <= 8:
        return number_of_coffees * price_per_coffee
    else:
        # Calculate the number of free coffees
        # Every 9th coffee is free, so we use integer division by 9
        free_coffees = number_of_coffees // 9
        
        # Subtract the free coffees from the total
        number_of_coffees -= free_coffees
        
        # Calculate and return the total cost
        return number_of_coffees * price_per_coffee

# Test cases
assert get_cost_of_coffee(7, 2.50) == 17.50
assert get_cost_of_coffee(8, 2.50) == 20
assert get_cost_of_coffee(9, 2.50) == 20
assert get_cost_of_coffee(10, 2.50) == 22.50

# Additional test cases for various prices
for i in range(1, 4):
    assert get_cost_of_coffee(0, i) == 0
    assert get_cost_of_coffee(8, i) == 8 * i
    assert get_cost_of_coffee(9, i) == 8 * i
    assert get_cost_of_coffee(18, i) == 16 * i
    assert get_cost_of_coffee(19, i) == 17 * i
    assert get_cost_of_coffee(30, i) == 27 * i