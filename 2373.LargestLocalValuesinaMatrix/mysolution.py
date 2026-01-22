class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        length = len(grid)
        ans = []
        for n in range(0, length - 2):
            ans.append([])
            for m in range(0, length - 2):
                ans[n].append(0)
        for i in range(0, length):
            for j in range(0, length):
                for n in range(1, length - 1):
                    for m in range(1, length - 1):
                        if grid[i][j] > ans[n - 1][m - 1] and i <= n + 1 and j <= m + 1 and i >= n - 1 and j >= m - 1:
                            ans[n - 1][m - 1] = grid[i][j]
        return ans