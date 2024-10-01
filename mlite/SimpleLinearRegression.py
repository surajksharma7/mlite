import numpy as np

class linearRegression:

    def __init__(self):
        self.intercept = None
        self.coef_ = None

    def fit(self, X_train, y_train):
        num = 0
        den = 0

        # Calculate numerator and denominator for slope (coefficient)
        for i in range(X_train.shape[0]):
            num += (X_train[i] - X_train.mean()) * (y_train[i] - y_train.mean())
            den += (X_train[i] - X_train.mean()) * (X_train[i] - X_train.mean())

        # Calculate the coefficient (slope)
        self.coef_ = num / den 
        
        # Calculate the intercept
        self.intercept = y_train.mean() - (self.coef_ * X_train.mean())

    def predict(self, X_test):
        # Predict values using the learned slope and intercept
        return self.intercept + self.coef_ * X_test
