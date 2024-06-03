from sympy import symbols, factorial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class BivariateBezierSurface:
    def __init__(self, control_points, var='b'):
        """
        Initializes a bivariate Bezier surface with the given control points.
        
        Parameters:
            control_points (2D list or np.ndarray): A matrix representing the control points of a Bezier surface.
        """
        # Ensure control_points is a 2D list or a 2D numpy array
        if not isinstance(control_points, (list, np.ndarray)) or np.array(control_points).ndim != 2:
            raise TypeError(f"Control points must be a 2D list or a 2D numpy array. Found {type(control_points)}")
        
        self.control_points = np.array(control_points)
        self.degree = self.control_points.shape[0] - 1  # Assuming square matrix of control points

    def basis(self, i, j, dg, u, v):
        """
        Initializes the Bernstein basis in the bivariate form.

        Parameters:
            i (int): Index of the basis function along the u-direction.
            j (int): Index of the basis function along the v-direction.
            dg (int): Degree of the Bezier surface.
            u (symbol): The parameter value along the u-direction.
            v (symbol): The parameter value along the v-direction.

        Returns:
            sympy expression: The Bernstein basis function.
        """
        w = 1 - u - v
        k = dg - i - j
        return factorial(dg) / (factorial(i) * factorial(j) * factorial(k)) * (u**i) * (v**j) * (w**k)

    def evaluate(self, u=symbols('u'), v=symbols('v')):
        """
        Evaluates the Bezier surface at parameters (u, v).

        Parameters:
            u (float): The parameter value along the u-direction.
            v (float): The parameter value along the v-direction.

        Returns:
            float: The point on the Bezier surface corresponding to the parameters (u, v).
        """
        point = 0
        for i in range(self.degree + 1):
            for j in range(self.degree + 1):
                point += self.control_points[i, j] * self.basis(i, j, self.degree, u, v)
        return point

    def plot(self, num_points=100, grid=True, fig=(8, 6)):
        """
        Plots the Bezier surface using matplotlib.

        Parameters:
            num_points (int): Number of points on the surface to calculate for plotting.
        """
        u_values = np.linspace(0, 1, num_points)
        v_values = np.linspace(0, 1, num_points)
        U, V = np.meshgrid(u_values, v_values)
        Z = np.array([[self.evaluate(u, v) for v in v_values] for u in u_values])
        
        fig = plt.figure(figsize=fig)
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(U, V, Z, cmap='viridis')

        ax.set_xlabel('u')
        ax.set_ylabel('v')
        ax.set_zlabel('z')
        ax.set_title('Bivariate Bezier Surface')
        plt.grid(grid)
        plt.show()
