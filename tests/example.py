from sympy import symbols, factorial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Import the BezierCurve and BivariateBezierSurface classes and utility functions
from bbpi import BezierCurve
from bbpi import add, multiply, degree_raise, subdivide, derivative
from bbpi import BivariateBezierSurface

def test():
    # Define control points
    control_points1 = [[0, 1, 2, 3], [0, 2, 1, 3]]
    control_points2 = [[0, -1, -2, -3], [0, -2, -1, -3]]

    # Create Bezier curves
    curve1 = BezierCurve(control_points1)
    curve2 = BezierCurve(control_points2)

    # Plot the first Bezier curve
    print("Plotting the first Bezier curve")
    curve1.plot()

    # Add the two Bezier curves
    print("Adding two Bezier curves")
    result_curve = add(curve1, curve2)
    result_curve.plot()

    # Multiply the two Bezier curves
    print("Multiplying two Bezier curves")
    multiplied_curve = multiply(curve1, curve2)
    multiplied_curve.plot()

    # Degree raise the first Bezier curve
    print("Degree raising the first Bezier curve")
    raised_curve = degree_raise(curve1)
    raised_curve.plot()

    # Subdivide the first Bezier curve at t = 0.5
    print("Subdividing the first Bezier curve at t = 0.5")
    left_curve, right_curve = subdivide(curve1, 0.5)
    left_curve.plot()
    right_curve.plot()

    # Compute the derivative of the first Bezier curve
    print("Computing the derivative of the first Bezier curve")
    derivative_curve = derivative(curve1)
    derivative_curve.plot()

    # Example usage for BivariateBezierSurface

    # Define control points for a bivariate Bezier surface
    control_points_surface = [
        [1, 2, 3, 2, 1],
        [2, 5, 7, 5, 2],
        [3, 7, 10, 7, 3],
        [2, 5, 7, 5, 2],
        [1, 2, 3, 2, 1]
    ]

    # Create a Bivariate Bezier surface
    surface = BivariateBezierSurface(control_points_surface)

    # Plot the Bivariate Bezier surface
    print("Plotting the Bivariate Bezier surface")
    surface.plot()

    assert True
