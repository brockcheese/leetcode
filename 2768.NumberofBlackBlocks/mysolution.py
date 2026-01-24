class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        matrix = []
        for i in range(m):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)
        for coordinate in coordinates:
            matrix[coordinate[0]][coordinate[1]] = 1
        ans = [0, 0, 0, 0, 0]
        for i in range(m - 1):
            for j in range(n - 1):
                ans[matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]] += 1
        return ans