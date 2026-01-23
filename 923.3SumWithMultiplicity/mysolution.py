class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        ans = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == target:
                        ans += 1
        return ans