def find_and_replace(text, old_text, new_text):
    """
    Replaces all occurrences of old_text with new_text in the given text.
    The function is case-sensitive and does not use built-in find or replace methods.
    
    Args:
    text (str): The original text to perform replacement on.
    old_text (str): The substring to be replaced.
    new_text (str): The substring to replace old_text with.
    
    Returns:
    str: The text after all replacements have been made.
    """
    replaced_text = ""
    i = 0
    while i < len(text):
        if text[i:(i + len(old_text))] == old_text:
            replaced_text += new_text
            i += len(old_text)
        else:
            replaced_text += text[i]
            i += 1
        
    return replaced_text

assert find_and_replace("The fox", "fox", "dog") == "The dog"
assert find_and_replace("fox", "fox", "dog") == "dog"
assert find_and_replace("Firefox", "fox", "dog") == "Firedog"
assert find_and_replace("foxfox", "fox", "dog") == "dogdog"
assert find_and_replace("The Fox and fox.", "fox", "dog") == "The Fox and dog."
assert find_and_replace("foofoofoo", "foo", "bar") == "barbarbar"
assert find_and_replace("foxfoofat", "foo", "bar") == "foxbarfat"