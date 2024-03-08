import math

def print_circle(radius):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            distance = math.sqrt(x**2 + y**2)
            if distance <= radius + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage:
circle_radius = 5
print_circle(circle_radius)
