class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        m = len(pattern)
        ans = 0
        for i in range(len(nums) - m):
            valid = True
            for k in range(m):
                if pattern[k] == 1:
                    if nums[i + k + 1] <= nums[i + k]:
                        valid = False
                        break
                elif pattern[k] == 0:
                    if nums[i + k + 1] != nums[i + k]:
                        valid = False
                        break
                else: 
                    if nums[i + k + 1] >= nums[i + k]:
                        valid = False
                        break
            if valid:
                ans += 1
        return ans