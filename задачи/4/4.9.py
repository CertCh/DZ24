import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def add(self, other):
        return Matrix(self.data + other.data)

    def subtract(self, other):
        return Matrix(self.data - other.data)

    def multiply(self, other):
        return Matrix(np.dot(self.data, other.data))

    def transpose(self):
        return Matrix(self.data.T)

    def determinant(self):
        return np.linalg.det(self.data)

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print("Sum:")
print(m1.add(m2).data)
print("Difference:")
print(m1.subtract(m2).data)
print("Product:")
print(m1.multiply(m2).data)
print("Transpose of m1:")
print(m1.transpose().data)
print("Determinant of m1:")
print(m1.determinant())
