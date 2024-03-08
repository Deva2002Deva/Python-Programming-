def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage:
test_number = 7
result = check_number(test_number)
print(f"The number {test_number} is {result}.")
