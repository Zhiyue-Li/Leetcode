def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    l = n - 1
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[l-j][i]
            matrix[l-j][i] = matrix[l-i][l-j]
            matrix[l-i][l-j] = matrix[j][l-i]
            matrix[j][l-i] = tmp