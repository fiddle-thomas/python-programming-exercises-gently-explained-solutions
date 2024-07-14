def get_hours_minutes_seconds(total_seconds):
    # Define constants for time conversions
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_min = 60

    # Calculate days and update total_seconds
    days = total_seconds // seconds_in_day
    if total_seconds >= seconds_in_day:
        total_seconds = total_seconds - seconds_in_day * days
    
    # Calculate hours and update total_seconds
    hours = total_seconds // seconds_in_hour
    if total_seconds >= seconds_in_hour:
        total_seconds = total_seconds - seconds_in_hour * hours
    
    # Calculate minutes and update total_seconds
    minutes = total_seconds // seconds_in_min
    if total_seconds >= seconds_in_min:
        total_seconds = total_seconds - seconds_in_min * minutes
    
    # Remaining seconds
    seconds = total_seconds 
        
    # Create a dictionary to store time units
    time_dict = {
        "d" : days,
        "h" : hours,
        "m" : minutes,
        "s" : seconds
    }

    # List to store formatted time strings
    time_string_parts = []

    # Iterate through the time dictionary
    for key, value in time_dict.items():
        # Special case: if seconds is 0 and no other units, add '0s'
        if key == "s" and value == 0 and not time_string_parts:
            time_string_parts.append(f"{value}{key}")
        # Skip if value is 0
        elif value == 0:
            continue
        # Add formatted string for non-zero values
        else:
            time_string_parts.append(f"{value}{key}")
    
    # Join the formatted time strings
    time_string = " ".join(time_string_parts)
    return time_string  # Return the resulting time string

# Test cases
assert get_hours_minutes_seconds(30)
assert get_hours_minutes_seconds(60)
assert get_hours_minutes_seconds(90)
assert get_hours_minutes_seconds(3600)
assert get_hours_minutes_seconds(3601)
assert get_hours_minutes_seconds(3661)
assert get_hours_minutes_seconds(90042)
assert get_hours_minutes_seconds(0)