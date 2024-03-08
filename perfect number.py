def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number

# Example usage:
test_number = 28
if is_perfect_number(test_number):
    print(f"{test_number} is a perfect number.")
else:
    print(f"{test_number} is not a perfect number.")
