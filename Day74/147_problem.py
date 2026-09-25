# Create a class Matrix with attribute data (a 2D list, e.g., [[1,2],[3,4]]). Add a method transpose() that returns the transposed matrix (rows become columns).


class Matrix:
    def __init__(self, data):
        self.data = data

    def transpose(self):
        return [list(row) for row in zip(*self.data)]


matrix = Matrix([[1, 2], [3, 4]])

print(matrix.transpose())