class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        direction = 0
        while len(matrix) > 0:
            if direction == 0:
                ans += matrix.pop(0)
                direction = 1
            elif direction == 1:
                for l in matrix:
                    ans.append(l.pop(len(l) - 1))
                direction = 2
            elif direction == 2:
                ans += matrix.pop(len(matrix) - 1)[::-1]
                direction = 3
            elif direction == 3:
                for l in matrix[::-1]:
                    ans.append(l.pop(0))
                direction = 0
        return ans