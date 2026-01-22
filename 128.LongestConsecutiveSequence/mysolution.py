class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        ans = 0
        for n in numSet:
            i = 1
            tempans = 1
            while(n + i in numSet):
                tempans += 1
                i += 1
            if tempans > ans:
                ans = tempans
        return ans