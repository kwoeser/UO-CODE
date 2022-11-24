import math
import random

def is_in_circle(x_coordinate: float, y_coordinate: float) -> bool:
    """
    This function determines if a point is within a circle centered at (0, 0)
    and has a radius of 1.

    The function will determine this by:
    (1) finding the distance "dist" between the given point and (0, 0)
    (2) determine if the distance "dist" is greater than 1
        (If dist > 1, the point is outside the circle.)

    param x_coordinate: The x coordinate of a point.
    param y_coordinate: The y coordinate of a point.
    return: True if the point (x_coordinate, y_coordinate) is inside a circle
    centered at (0, 0) with radius 1; otherwise returns False.

    >>> is_in_circle(0.1, 0.1)
    True

    >>> is_in_circle(1.0, 1.0)
    False
    """
    # Complete the function here.
    # Reminder that the distance between a point(x,y) and (0, 0) is √(x² + y²)
    dist = math.sqrt(x_coordinate**2 + y_coordinate**2)
    result = dist <= 1
    return result





def monte_pi(number_of_darts: int) -> float:
    """
    This function approximates pi using a Monte Carlo method.

    The function approximates pi by randomly "throwing darts" at a circle inside
    a square board.

    Recall that:
    pi_approx = 4 * (number_of_darts_in_circle / total_number_of_darts_thrown)

    This function will call "is_in_circle( ... )" to help calculate the variable
    "number_of_darts_in_circle".

    param number_of_darts: The number of darts to throw.
    return: An approximation of pi.

    >>> monte_pi(10)
    # A very bad approximation of pi. A specific number can be determined by setting random.seed().

    >>> monte_pi(1000)
    # A bad approximation of pi. A specific number can be determined by setting random.seed().
    """
    # Complete the function here.

    count = 0
    for _ in range(number_of_darts):
        rand_x_coord = random.random()
        rand_y_coord = random.random()

        if is_in_circle(rand_x_coord, rand_y_coord):
            count += 1
        
    pi_approx = 4 * (count / number_of_darts)
    return pi_approx


print(monte_pi(10))
print(monte_pi(1000))
print(monte_pi(1000000))
