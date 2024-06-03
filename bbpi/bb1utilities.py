from bbpi.bb1curve import BezierCurve
from sympy import binomial
import numpy as np


def add(curve1, curve2):
        """
        Adds the coefficients of two univariate bezier curves
        
        Parameters:
        degree (integer): the degree of the new curve.
        curve1 (BezierCurve): The first Bezier curve.
        curve2 (BezierCurve): The second Bezier curve.

        Returns:
        out: A new Bezier curve resulting from the addition of the control points of the two curves.
        """
        if curve1.control_points.shape[0] != curve2.control_points.shape[0]:
            raise ValueError(f"dimensions do not match. Curve 1: {curve1.control_points.shape[0]} , Curve 2: {curve1.control_points.shape[0]}")
        

        if(curve1.degree == curve2.degree):
                # Initialize an empty matrix with the same number of rows as control_points and columns as degree + 1
            out = [[0 for _ in range(curve1.degree + 1)] for _ in range(curve1.control_points.shape[0])]

            for dimension, row in enumerate(out):
                
                for i, (element1, element2) in enumerate(zip(curve1.control_points[dimension],curve2.control_points[dimension])):
                    out[dimension][i] += element1 + element2
                    # for j, coefficient in enumerate(curve1.control_points[dimension]):
                    #     print(f"coefficient[{j}]: {coefficient}")
                    #     out[dimension][i] += coefficient

                    # for k, coefficient in enumerate(curve2.control_points[dimension]):
                    #     print(f"coefficient[{k}]: {coefficient}")
                    #     out[dimension][i] += coefficient


            print(out)
                # Convert the output list of lists into a numpy array for the new curve
            return BezierCurve(np.array(out))
        else:
            raise ValueError(f"degrees of the two curves do not match, found {curve1.degree} and {curve2.degree}")
        
def multiply(curve1,curve2,lo=None, hi=None):
    """
    Multiply two univariate polynomials in BB-form

    Parameters:
    curve1 -- array of coefficients of polynomial 1
    d1 -- degree of polynomial 1
    curve2 -- array of coefficients of polynomial 2
    d2 -- degree of polynomial 2
    lo -- (optional) lower index of vectors for component-wise multiplication
    hi -- (optional) upper index of vectors for component-wise multiplication

    Returns:
    out -- array of coefficients of the product polynomial in BB-form
    """
    if curve1.control_points.shape[0] != curve2.control_points.shape[0]:
        raise ValueError(f"Found different dimensions: curve 1: {curve1.control_points.shape[0]} curve 2: {curve2.control_points.shape[0]}")
    
    dgout = curve1.degree + curve2.degree
    out = [[0 for _ in range(dgout + 1)] for _ in range(curve1.control_points.shape[0])]
    for dimension, row in enumerate(out): 
        if lo is None or hi is None:
            for i1 in range(curve1.degree + 1):
                for i2 in range(curve2.degree + 1):
                    mult = binomial(curve1.degree, i1) * binomial(curve2.degree, i2) / binomial(curve1.degree+curve2.degree, i1 + i2)
                    out[dimension][i1 + i2] += mult * curve1.control_points[dimension][i1] * curve2.control_points[dimension][i2]
        else:
            for i1 in range(curve1.degree + 1):
                for i2 in range(curve2.degree + 1):
                    mult = binomial(curve1.degree, i1) * binomial(curve2.degree, i2) / binomial(curve1.degree+curve2.degree, i1 + i2)
                    h = sum(curve1.b[m][i1] + curve2.b[m][i2] for m in range(lo, hi + 1))
                    out[dimension][i1 + i2] += mult * h

    return BezierCurve(np.array(out))

def degree_raise(curve):
    """
    raise the degree of a bezier curve by 1

    Parameters:
    curve -- array of coefficients 

    Returns:
    out -- bezier curve with degree + 1
    """
    d1 = curve.degree + 1

    out = [[0 for _ in range(d1 + 1)] for _ in range(curve.control_points.shape[0])]

    for dimension, row in enumerate(out):
        for i in range(d1+1):
            if 0 < i:
                out[dimension][i] += i * curve.control_points[dimension][i-1] /d1
            if i <= curve.degree:
                out[dimension][i] += (d1 - i) * curve.control_points[dimension][i] /d1
            
    return BezierCurve(np.array(out))
    
def subdivide(curve, s=0.5):
        """
        Subdivide the Bezier curve at a parameter s, returning two new Bezier curves.
        
        :param s: The parameter at which to subdivide the curve, typically in [0, 1].
        :return: A tuple containing two new BezierCurve instances representing the subdivided curves.
        """
        dg = curve.degree
        b_local = np.copy(curve.control_points)
        bl = [[0 for _ in range(dg + 1)] for _ in range(curve.control_points.shape[0])]
        br = [[0 for _ in range(dg + 1)] for _ in range(curve.control_points.shape[0])]
        for dimension, row in enumerate(curve.control_points):
            

            bl[dimension][0] = b_local[dimension][0]
            br[dimension][dg] = b_local[dimension][dg]
            for l in range(1, dg+1):
                for i in range(dg+1-l):
                    b_local[dimension][i] = (1-s) * b_local[dimension][i] + s * b_local[dimension][i+1]
                bl[dimension][l] = b_local[dimension][0]
                br[dimension][dg-l] = b_local[dimension][dg-l]

            return BezierCurve(bl), BezierCurve(br)
        
def integral(curve):
    x = 1

def derivative(curve):
    """
    Compute the derivative of a Bezier curve and replaces the control points 
    , which is a Bezier curve of degree n-1

    Returns:
        BezierCurve: A new Bezier curve representing the derivative.
    """
    n = curve.degree
    
    derived_control_points = np.array([[n * (curve.control_points[dim][i + 1] - curve.control_points[dim][i]) for i in range(n)] for dim in range(curve.control_points.shape[0])])
    curve.control_points = derived_control_points
    

    return BezierCurve(derived_control_points)




