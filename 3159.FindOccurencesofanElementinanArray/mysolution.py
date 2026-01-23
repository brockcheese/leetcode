class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        positions = []
        ans = []
        for i in range(0, len(nums)):
            if nums[i] == x:
                positions.append(i)
        positionLen = len(positions)
        for n in queries:
            if n - 1 < positionLen:
                ans.append(positions[n - 1])
            else:
                ans.append(-1)
        return ans