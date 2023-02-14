def backtrack(matrix):
    if is_solved(matrix):
        return matrix

    for row in range(4):
        for col in range(4):
            if matrix[row][col] == 0:
                for value in range(1,5):
                    if is_valid(matrix, row, col, value):
                        matrix[row][col] = value
                        result = backtrack(matrix)
                        if result is not None:
                            return result
                return None

def is_solved(matrix):
    for row in range(4):
        for col in range(4):
            if matrix[row][col] == 0:
                return False
    return True

def is_valid(matrix, row, col, value):
    for i in range(4):
        if matrix[row][i] == value or matrix[i][col] == value:
            return False
    return True

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

matrix = [
    [0, 3, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 0, 0]
]


print_matrix(backtrack(matrix))