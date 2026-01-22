class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        ans = 0
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    for l in nums4:
                        if i + j + k + l == 0:
                            ans += 1
        return ans