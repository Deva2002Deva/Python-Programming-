def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Example usage:
number_of_terms = 10
fibonacci_result = generate_fibonacci(number_of_terms)
print(f"The Fibonacci sequence up to {number_of_terms} terms is: {fibonacci_result}")
