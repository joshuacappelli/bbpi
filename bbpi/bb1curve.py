from sympy import symbols, factorial, binomial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



class BezierCurve:
    def __init__(self, control_points, var='b'):
        """
        Initializes a univariate bezier curve with the given control points
        
        Parameters:
            control_points (list): A list representing the control points of a bezier curve
        """
        # Ensure control_points is a list or a numpy array
        if not isinstance(control_points, (list, np.ndarray)):
            raise TypeError(f"Control points must be a list or a numpy array. Found {type(control_points)}")
        
        self.control_points = np.atleast_2d(np.array(control_points))

        if self.control_points.ndim > 3:
            raise ValueError(f"control points cannot have more than 3 rows, found {self.control_points.ndim}")
        
        self.degree = self.control_points.shape[1]-1
        self.dimension = self.control_points.shape[0]

        if self.control_points.shape[0] > 1:
            self.b = [[symbols(f'{var}_{i}_{j}') for j in range(self.degree + 1)] for i in range(self.control_points.shape[0])]
        else:
            self.b = [[symbols(f'{var}_{i}') for i in range(self.degree+1)]]


    def basis(self, i , u):
        """
        Initializes the bernstein basis in the univariate form

        Parameters:
            u (symbol): representing the variable in the basis function
            i (integer): the index of the basis function
        Returns:
            symbolic representation of the basis function at index i
        """
        
        j = self.degree - i
        b = (factorial(self.degree) / (factorial(j) * factorial(i))) * (1 - u)**j * u**i
        return b

    
    def evaluate(self, t = symbols('u')):
        """
        Evaluates the Bezier curve at parameter t using the De Casteljau's algorithm.

        Parameters:
            t (float): The parameter value (typically between 0 and 1).

        Returns:
            np.array: The point on the Bezier curve corresponding to the parameter t.
        """
        point = [0] * self.control_points.shape[0]
        
        points = np.array(self.control_points)
        
        for i, row in enumerate(points):
            p = [0]
            for j, element in enumerate(row):
                p[0] +=  element * self.basis(j,t)
            point[i] = p 
        
        return np.array(point).astype(np.float64)

    def plot(self, num_points=100, grid=True, fig=(8,6)):
        """
        Plots the Bezier curve using matplotlib.

        Parameters:
            num_points (int): Number of points on the curve to calculate for plotting.
        """
        if self.control_points.shape[0] >= 2:
            t_values = np.linspace(0, 1, num_points)
            curve_points = np.array([self.evaluate(t) for t in t_values])
            
            plt.figure(figsize=fig)
            plt.plot(curve_points[:,0], curve_points[:,1], label="Bezier Curve")
            plt.scatter(self.control_points[0, :], self.control_points[1, :], color='red', label="Control Points")
            plt.plot(self.control_points[0, :], self.control_points[1, :], 'r--', label="Control Polygon")
            plt.legend()
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Bezier Curve")
            plt.grid(grid)
            plt.show()

    def plot3D(self, num_points=100, f=111, color='r', mark='o', xlabel='X coordinate', ylabel='Y coordinate', zlabel='Z coordinate', cp = True, crve = True):
        fig = plt.figure()
        ax = fig.add_subplot(f, projection='3d')
        
        if self.control_points.shape[0] != 3:
            raise ValueError(f"wrong dimension, needed 3 found {self.control_points.shape[0]}")

        t_values = np.linspace(0, 1, num_points)
        print(type(self.control_points))
        curve_points = np.array([self.evaluate(t) for t in t_values])
        if(cp == True):
            ax.scatter3D(self.control_points[0, :], self.control_points[1, :], self.control_points[2, :], c=color, marker=mark)

        if(crve == True):
            ax.plot(curve_points[:,0],curve_points[:,1],curve_points[:,2])
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        plt.show()

        


    def add_control_point(self, point):
        """
        Adds a new control point to the Bezier curve.

        Parameters:
            point integer: A tuple (x, y) representing the new control point to be added.
        """
        #TODO fix adding
        self.control_points = np.vstack([self.control_points, point])

    def modify_control_point(self, index, new_point):
        """
        Modifies an existing control point in the Bezier curve.

        Parameters:
            index (int): The index of the control point to modify.
            new_point (tuple): A tuple (x, y) representing the new value of the control point.
        """
        if 0 <= index < len(self.control_points):
            self.control_points[index] = new_point
        else:
            raise IndexError("Control point index is out of range.")
