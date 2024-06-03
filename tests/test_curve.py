import numpy as np
from sympy import symbols
import pytest
from bbpi import BezierCurve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def test_initialization0():
    control_points = [1,2,3]
    index = 1
    u = symbols('u')
    basis1 = u*(2-2*u)
    curve = BezierCurve(control_points)
    basis2 = curve.basis(index,u)
    print(type(curve.control_points))
    assert basis1 == basis2
    assert curve.degree == 2
    assert curve.dimension == 1

def test_initialization1():
    control_points = [[1,2,3],[4,5,6]]
    index = 1
    u = symbols('u')
    basis1 = u*(2-2*u)
    curve = BezierCurve(control_points)
    basis2 = curve.basis(index,u)

    assert curve.degree == 2
    assert curve.dimension == 2
    assert basis1 == basis2

def test_evaluation2():
    control_points = [1,0,1]
    u = 0.5
    curve = BezierCurve(control_points)
    eval = curve.evaluate(u)
    assert eval == [0.5]

def test_evaluation3():
    control_points = [[1,0,1],[1,0,1]]
    u = 0.5
    curve = BezierCurve(control_points)
    eval = curve.evaluate(u)
    print(eval)
    assert np.allclose(eval,np.array([0.5,0.5]))

def test_evaluation4():
        curve = BezierCurve([2,2,0,-2,-2])
        curve2 = BezierCurve([0,1,2,1,0])
        eval = curve.evaluate(0.2)
        eval2 = curve2.evaluate(0.2)
        curve3 = BezierCurve([[2,2,0,-2,-2],[0,1,2,1,0]])
        eval3 = curve3.evaluate(0.2)
        print(f"eval 1: {eval}    eval 2: {eval2}   eval 3: {eval3}")
        assert True

def test_plot5():
    control_points = [[1,2,3],[4,5,6]]
    curve = BezierCurve([[2,2,0,-2,-2],[0,1,2,1,0]])    
    print(curve.control_points[0,:])
    print(curve.control_points[1,:])
    curve.plot()
    assert True

def test_3D():
    points = 20
    x =np.random.rand(points)
    y =np.random.rand(points)
    z =np.random.rand(points)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x,y,z,c='b',marker='o')

    ax.set_xlabel('x')
    ax.set_xlabel('y')
    ax.set_xlabel('z')
    ax.set_title('random points')

    plt.show()


def test_3dplot():
    curve = BezierCurve([[2,2,0,-2,-2],[0,1,2,1,0],[1,2,3,4,5]])
    curve.plot3D()
    assert False
