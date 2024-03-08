def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
test_number = 9
result = check_even_odd(test_number)
print(f"The number {test_number} is {result}.")
