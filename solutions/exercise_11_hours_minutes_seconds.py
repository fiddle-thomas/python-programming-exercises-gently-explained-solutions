def get_hours_minutes_seconds(total_seconds):
    # Constants for time unit conversions
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_min = 60

    # List to store formatted time units
    time = []

    # Check and format days
    if total_seconds >= seconds_in_day:
        time.append(f"{total_seconds // seconds_in_day}d")
        total_seconds = total_seconds % seconds_in_day

    # Check and format hours
    if total_seconds >= seconds_in_hour:
        time.append(f"{total_seconds // seconds_in_hour}h")
        total_seconds = total_seconds % seconds_in_hour

    # Check and format minutes
    if total_seconds >= seconds_in_min:
        time.append(f"{total_seconds // seconds_in_min}m")
        total_seconds = total_seconds % seconds_in_min

    # Handle remaining seconds or the case when all larger units are zero
    if not time or total_seconds > 0:
        time.append(f"{total_seconds}s")

    # Join the formatted time units into a single string
    time_string = " ".join(time)
    return time_string

# Assert statements to verify the function's correctness
assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '1d 1h 42s'
assert get_hours_minutes_seconds(0) == '0s'