# mlite/regression.py

import numpy as np

def linear_regression(X, y):
    """
    Perform simple linear regression (one feature).
    
    Parameters:
    X (np.array): Feature array (1D or 2D with one feature).
    y (np.array): Target values.

    Returns:
    Tuple (slope, intercept): The coefficients for the best-fit line.
    """
    X = np.array(X)
    y = np.array(y)
    
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    
    # Add bias term (column of ones)
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    
    # Closed form solution (normal equation)
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    intercept = theta_best[0]
    slope = theta_best[1:]
    
    return slope, intercept

def multiple_linear_regression(X, y):
    """
    Perform multiple linear regression (multiple features).
    
    Parameters:
    X (np.array): Feature matrix (2D with multiple features).
    y (np.array): Target values.
    
    Returns:
    np.array: The coefficients (including intercept).
    """
    X = np.array(X)
    y = np.array(y)
    
    # Add bias term (column of ones)
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    
    # Closed form solution (normal equation)
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    return theta_best
