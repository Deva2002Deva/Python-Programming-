def print_triangle(height):
    for i in range(1, height + 1):
        spaces = height - i
        print(" " * spaces + "*" * (2 * i - 1))

# Example usage:
triangle_height = 5
print_triangle(triangle_height)
