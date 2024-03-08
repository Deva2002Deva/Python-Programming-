def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    clean_str = ''.join(input_str.split()).lower()

    # Check if the cleaned string is the same when reversed
    return clean_str == clean_str[::-1]

# Example usage:
word = "radar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
