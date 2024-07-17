def is_leap_year(year):
    # A year is a leap year if it meets the following conditions:
    # 1. It's divisible by 4 AND
    # 2. It's either:
    #    a) Not divisible by 100 OR
    #    b) Divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)