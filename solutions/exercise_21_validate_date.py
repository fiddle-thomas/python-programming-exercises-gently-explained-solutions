from exercise_20_leap_year import is_leap_year

# Dictionary defining the number of days in each month (non-leap year)
calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def is_valid_date(year, month, day):
    """
    Validates if the given year, month, and day represent a valid date.
    
    This function checks if the input represents a valid date by considering:
    - The year must be positive
    - The month must be between 1 and 12
    - The day must be valid for the given month, accounting for leap years in February
    
    Args:
    year (int): The year to validate (must be positive)
    month (int): The month to validate (1-12)
    day (int): The day to validate (1-31, depending on the month)
    
    Returns:
    bool: True if the date is valid, False otherwise
    
    Note:
    This function uses the is_leap_year function imported from exercise_20_leap_year.py
    to determine if February should have 29 days in the given year.
    """
    if 1 <= month <= 12 and year > 0:
        return (month == 2 and ((1 <= day <= calendar[month]) or (is_leap_year(year) and 1 <= day <= 29))) or (month != 2 and 1 <= day <= calendar[month])
    else:
        return False

# Test assertions
assert is_valid_date(1999, 12, 31) == True
assert is_valid_date(2000, 2, 29) == True
assert is_valid_date(2001, 2, 29) == False
assert is_valid_date(2029, 13, 1) == False
assert is_valid_date(1000000, 1, 1) == True
assert is_valid_date(2015, 4, 31) == False
assert is_valid_date(1970, 5, 99) == False
assert is_valid_date(1981, 0, 3) == False
assert is_valid_date(1666, 4, 0) == False

# Additional test: Check a million consecutive dates
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert is_valid_date(d.year, d.month, d.day) == True
    d += oneDay