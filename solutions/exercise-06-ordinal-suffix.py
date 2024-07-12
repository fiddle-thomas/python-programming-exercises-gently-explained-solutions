# Function to return the ordinal suffix for a given number
def ordinal_suffix(number):
    # Convert the number to a string for easier manipulation
    num_str = str(number)
    
    # Check if the last two digits are 11, 12, or 13, or any number ending in 11, 12, 13
    if len(num_str) > 1 and num_str[-2] == "1":
        return num_str + "th"
    else:
        # Determine the suffix based on the last digit of the number
        if num_str[-1] == "1":
            return num_str + "st"  # Numbers ending in 1 (except for those covered above) use "st"
        elif num_str[-1] == "2":
            return num_str + "nd"  # Numbers ending in 2 (except for those covered above) use "nd"
        elif num_str[-1] == "3":
            return num_str + "rd"  # Numbers ending in 3 (except for those covered above) use "rd"
        else:
            return num_str + "th"  # All other numbers use "th"

# Test cases to verify the correctness of the ordinal_suffix function
assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'
