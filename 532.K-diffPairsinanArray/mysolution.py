class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        myDict = dict()
        ans = 0
        for num in nums:
            if num in myDict.keys():
                myDict[num] += 1
            else:
                myDict[num] = 1
        for num in myDict.keys():
            if k == 0:
                if myDict[num] > 1:
                    ans += 1
            elif num + k in myDict.keys():
                ans += 1
        return ans