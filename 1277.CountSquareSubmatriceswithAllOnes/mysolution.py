class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        ans = 0
        length = len(matrix)
        for i in range(0, length):
            lengthi = len(matrix[i])
            for j in range(0, lengthi):
                square = 1
                while square != 0:
                    for size in range(0, square):
                        if j + size >= lengthi or i + size >= length or matrix[i][j + size] == 0 or matrix[i + size][j] == 0:
                            square = 0
                    if square != 0:
                        ans += 1
                        square += 1
        return ans
