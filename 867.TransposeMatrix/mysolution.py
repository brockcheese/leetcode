class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ans = []
        for i in range(0, len(matrix[0])):
            ans.append([])
            for j in range(0, len(matrix)):
                ans[i].append(matrix[j][i])
        return ans