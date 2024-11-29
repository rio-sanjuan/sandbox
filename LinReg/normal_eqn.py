import numpy as np

coef = np.random.rand(2, 1).reshape(-1)

n = int(1e5)
X = np.c_[np.ones((n, 1)), 2 * np.random.rand(n, 1)]
y = coef.dot(X.T).reshape(-1, 1) + np.random.randn(n, 1)

# theta = (X^T X)^-1 X^T y
theta_best = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
np.c_[coef, theta_best.reshape(-1)]
