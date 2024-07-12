# Function to find and replace occurrences of old_text with new_text in the given text
def find_and_replace(text, old_text, new_text):
    # Use the replace() method to replace all occurrences of old_text with new_text
    return text.replace(old_text, new_text)

# Assertions to test the function with various cases
assert find_and_replace("The fox", "fox", "dog") == "The dog"
assert find_and_replace("fox", "fox", "dog") == "dog"
assert find_and_replace("Firefox", "fox", "dog") == "Firedog"
assert find_and_replace("foxfox", "fox", "dog") == "dogdog"
assert find_and_replace("The Fox and fox.", "fox", "dog") == "The Fox and dog."
