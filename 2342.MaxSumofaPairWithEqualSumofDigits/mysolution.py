class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        myDict = dict()
        for num in nums:
            digitSum = 0
            temp = num
            while temp > 0:
                digitSum += temp % 10
                temp //= 10
            if digitSum not in myDict.keys():
                myDict[digitSum] = []
                myDict[digitSum].append(num)
            else:
                myDict[digitSum].append(num)
        ans = -1
        for key in myDict.keys():
            if len(myDict[key]) > 1:
                myDict[key].sort()
                temp = myDict[key][-1] + myDict[key][-2]
                if temp > ans:
                    ans = temp
        return ans