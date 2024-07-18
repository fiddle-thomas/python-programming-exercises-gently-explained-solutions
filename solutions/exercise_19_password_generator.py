import random

def generate_password(length):
    # Ensure minimum length of 12
    if length < 12:
        length = 12

    # Define pools of characters
    pool = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "~!@#$%^&*()_+"]

    password = []

    # Ensure at least one character from each pool
    for index in range(len(pool)):
        password.append(random.choice(pool[index]))

    # Fill the rest of the password with random characters from any pool
    while len(password) < length:
        password.append(random.choice(pool[random.randrange(len(pool))]))

    # Shuffle the password for added randomness
    random.shuffle(password)
    
    # Convert list to string and return
    return "".join(password)

# Define character sets for testing
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = "~!@#$%^&*()_+"

# Test cases to verify password generation
assert len(generate_password(8)) == 12
pw = generate_password(14)
assert len(pw) == 14

# Check if password contains all required character types
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial