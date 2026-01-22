class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        ans = 0
        for i in range(0, len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    ans += 1
        return ans