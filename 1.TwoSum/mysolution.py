class Solution:

    def quickSort(self, nums: List[int]) -> List[int]:
        if (len(nums) <= 1):
            return nums
        firstHalf = []
        secondHalf = []
        num = nums[0]
        for i in range(1, len(nums)):
            if (num > nums[i]):
                firstHalf.append(nums[i])
            else:
                secondHalf.append(nums[i])
        firstHalf = self.quickSort(firstHalf)
        secondHalf = self.quickSort(secondHalf)
        firstHalf.append(num)
        firstHalf.extend(secondHalf)
        return firstHalf

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = self.quickSort(nums)
        print(sortedNums)
        i = 0
        j = len(sortedNums) - 1
        while sortedNums[i] + sortedNums[j] != target:
            if sortedNums[j] + sortedNums[i] > target:
                j -= 1
            elif sortedNums[j] + sortedNums[i] < target:
                i += 1
        ans = []
        for ans1 in range(len(nums)):
            if nums[ans1] == sortedNums[i]:
                ans.append(ans1)
                break
        for ans2 in range(len(nums)):
            if nums[ans2] == sortedNums[j] and ans2 not in ans:
                ans.append(ans2)
                break
        return ans
