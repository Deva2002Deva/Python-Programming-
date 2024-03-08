import math

def calculate_pythagorean(hypotenuse=None, adjacent=None, opposite=None):
    if hypotenuse is not None and adjacent is not None and opposite is None:
        # Calculate opposite side
        opposite = math.sqrt(hypotenuse**2 - adjacent**2)
        return hypotenuse, adjacent, opposite
    elif hypotenuse is not None and opposite is not None and adjacent is None:
        # Calculate adjacent side
        adjacent = math.sqrt(hypotenuse**2 - opposite**2)
        return hypotenuse, adjacent, opposite
    elif adjacent is not None and opposite is not None and hypotenuse is None:
        # Calculate hypotenuse
        hypotenuse = math.sqrt(adjacent**2 + opposite**2)
        return hypotenuse, adjacent, opposite
    else:
        return None  # Insufficient information provided

# Example usage:
result = calculate_pythagorean(hypotenuse=5, adjacent=3)
print(f"Hypotenuse: {result[0]}, Adjacent: {result[1]}, Opposite: {result[2]}")
