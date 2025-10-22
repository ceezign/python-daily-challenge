# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# The area of a circle is defined as πr^2. Estimate π to 3 decimal
# places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2= r2.

import random

def estimate_pi(num_points=1000000):
    inside_circle = 0

    for _ in range(num_points):
        # Generate random (x, y) between -1 and 1
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        # Check if point is inside the circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # estimate pi
    pi_estimate = 4 * inside_circle / num_points
    return round(pi_estimate, 3)

# example usage
print("Estimated pi:", estimate_pi(1000000))

# Good morning! Here's your coding interview problem for today.
# This problem was asked by Facebook.
# Given a stream of elements too large to store in memory, pick a random
# element from the stream with uniform probability.

import random

def reservoir_sampling(stream):
    result = None
    for i, element in enumerate(stream, start=1):
        # with probability 1/1, replace result
        if random.randint(1, i) == 1:
            result = element
    return result

# Example usage
stream = range(1, 100001) # imagine a huge stream
print("Random element:", reservoir_sampling(stream))