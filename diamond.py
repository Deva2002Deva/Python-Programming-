def print_diamond(height):
    if height % 2 == 0:
        height += 1  # Make sure the height is an odd number for symmetry

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# Example usage:
diamond_height = 5
print_diamond(diamond_height)
