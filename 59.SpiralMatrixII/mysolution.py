import math
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = []
        i = 0
        j = 0
        direction = 0
        size = n * n
        for row in range(0,n):
            ans.append([])
            for column in range(0,n):
                ans[row].append(0)
        for digit in range(1, size + 1):
            ans[i][j] = digit
            if direction == 0:
                if j < n - 1 and ans[i][j+1] == 0:
                    j += 1 
                else:
                    i += 1
                    direction = 1
            elif direction == 1:
                if i < n - 1 and ans[i+1][j] == 0:
                    i += 1
                else:
                    j -= 1
                    direction = 2
            elif direction == 2:
                if j > 0 and ans[i][j-1] == 0:
                    j -= 1
                else:
                    i -= 1
                    direction = 3
            elif direction == 3:
                if i > 0 and ans[i-1][j] == 0:
                    i -= 1
                else:
                    j += 1
                    direction = 1
        return ans