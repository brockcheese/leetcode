class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        smallest = heights[0]
        index = 0
        left = 0
        right = 0
        for i, height in enumerate(heights):
            if height < smallest:
                smallest = height
                index = i
        ans = smallest * n
        if index > 0:
            left = self.largestRectangleArea(heights[0:index])
        if index < n - 1:
            right = self.largestRectangleArea(heights[index + 1:])
        if left > ans:
            ans = left
        if right > ans:
            ans = right
        return ans