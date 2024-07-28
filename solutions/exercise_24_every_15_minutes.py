# Loop through AM and PM
for meridiem in ("am", "pm"):
    # Loop through hours 0 to 11 (12-hour clock)
    for hour in range(12):
        # Loop through each quarter of an hour
        for quarter in (0, 15, 30, 45):
            # Special case for midnight/noon (0th hour)
            if hour == 0:
                print(f"12:{quarter:02} {meridiem}")
            else:
                # For all other hours, use the hour value directly
                print(f"{hour}:{quarter:02} {meridiem}")