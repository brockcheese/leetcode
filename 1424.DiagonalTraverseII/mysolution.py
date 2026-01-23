class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        maxi = 0
        maxj = 0
        ans = []
        length = len(nums)
        for i in range(0, length):
            rowLength = len(nums[i])
            if rowLength > maxj:
                maxj = rowLength
        maxi = i
        for i in range(0, maxi + maxj):
            if i >= length:
                row = length - 1
                col = i - row
            else:
                row = i
                col = 0
            while row >= 0:
                if length > row and len(nums[row]) > col:
                    ans.append(nums[row][col])
                row -= 1
                col += 1
        return ans