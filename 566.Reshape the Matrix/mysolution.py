class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        ans = []
        for n in range(0, r):
            ans.append([])
        i = 0
        j = 0
        for n in range (0, r):
            for m in range (0, c):
                if j == len(mat[0]):
                    j = 0
                    i += 1
                ans[n].append(mat[i][j])
                j += 1
        return ans