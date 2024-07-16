def is_leap_year(year):
    # A year is a leap year if it meets the following conditions:
    # 1. It's divisible by 4 AND
    # 2. It's either:
    #    a) Not divisible by 100 OR
    #    b) Divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Test cases
assert is_leap_year(1999) == False
assert is_leap_year(2000) == True
assert is_leap_year(2001) == False
assert is_leap_year(2004) == True  
assert is_leap_year(2100) == False
assert is_leap_year(2400) == True 