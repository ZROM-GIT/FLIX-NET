import numpy as np

class LinearRegression(object):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def fit(self):
        # Add a bias (intercept) term to the training data
        X_train_with_bias = np.vstack([np.ones(len(self.X)), self.X]).T

        # Calculate thetas (parameters) using the Normal Equation
        theta = np.linalg.inv(X_train_with_bias.T @ X_train_with_bias) @ X_train_with_bias.T @ self.y

        return theta



