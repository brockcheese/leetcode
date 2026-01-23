class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        n = 0
        while n < len(nums):
            while n < len(nums) and nums[n] % 2 != 1:
                n += 1
            m = n
            count = 1
            while count < k and m < len(nums):
                m += 1
                if m < len(nums) and nums[m] % 2 == 1:
                    count += 1
            if m >= len(nums):
                return ans
            leftIndex = n - 1
            left = 1
            while leftIndex > -1 and nums[leftIndex] % 2 != 1:
                leftIndex -= 1
                left += 1
            rightIndex = m + 1
            right = 1
            while rightIndex < len(nums) and nums[rightIndex] % 2 != 1:
                rightIndex += 1
                right += 1
            ans += left * right
            n += 1
        return ans