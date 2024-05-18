import numpy as np

class LinearEquationsSolver:
    def __init__(self, A, b):
        self.A = np.array(A)
        self.b = np.array(b)

    def solve(self):
        return np.linalg.solve(self.A, self.b)

A = [[2, 1], [1, 3]]
b = [8, 13]
solver = LinearEquationsSolver(A, b)
solution = solver.solve()
print(solution)
