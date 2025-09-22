import numpy as np

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * X**2 + 2 * X - X**3 + np.random.randn(100, 1) * 10

print(y)