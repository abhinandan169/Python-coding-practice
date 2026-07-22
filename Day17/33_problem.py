# Given a 2D list (matrix), print its transpose (swap rows and columns).
# Example: [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]

matrix = [[1,2,3],[4,5,6]]
result = []

for i in range(len(matrix[0])):
    new_row = []
    for j in range(len(matrix)):
        new_row.append(matrix[j][i])
    result.append(new_row)

print(result)