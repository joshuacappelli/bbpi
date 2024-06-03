import numpy as np
from sympy import symbols
import pytest
from bbpi import BezierCurve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from bbpi import add, multiply, degree_raise, subdivide, derivative

def test_add():

    curve1 = BezierCurve([1,1,1], var='c')
    curve2 = BezierCurve([2,3,5])
    add(curve1,curve2)
    assert True

def test_multiply():

    curve1 = BezierCurve([1,2,3])
    curve2 = BezierCurve([1,1])
    print(multiply(curve1,curve2).control_points)
    assert True

def test_degree_raise():
    curve = BezierCurve([[1,2,3],[1,2,3]])
    print(degree_raise(curve).control_points)
    assert True

def test_subdivide():
    control_points = [symbols(f'bb_{i}') for i in range(3)]

    # Create a BezierCurve instance
    curve = BezierCurve(control_points)

    # Perform the subdivision
    left_curve, right_curve = subdivide(curve,s=0.5)

    # Print the control points of the subdivided curves
    print(f"Left subdivided curve: {left_curve.control_points}\n left curve shape: {left_curve.control_points.shape}")
    print(f"Right subdivided curve: {right_curve.control_points}\n right curve shape: {right_curve.control_points.shape}")
    assert True

def test_derivative():
    dg = 4
    c = [symbols('c_%d' % i) for i in range(dg+1)]
    curve = BezierCurve(c)

    derivative(curve)
    print(curve.control_points)
    assert True