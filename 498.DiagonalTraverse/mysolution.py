class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        ans = []
        reverse = False
        length = len(mat) - 1
        for n in range(0, (length * 2) + 1):
            if reverse:
                i = 0
                j = n
            else:
                i = n
                j = 0
            for number in range(0, n + 1):
                if i <= length and j <= length:
                    ans.append(mat[i][j])
                if reverse:
                    i += 1
                    j -= 1
                else:
                    j += 1
                    i -= 1
            reverse = not reverse
        return ans