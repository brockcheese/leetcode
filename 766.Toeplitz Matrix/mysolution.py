class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        row1 = matrix[0]
        for row in range(1, len(matrix)):
            for i in range(1, len(matrix[row])):
                if matrix[row][i] != row1[i - 1]:
                    return False
            row1 = matrix[row]
        return True