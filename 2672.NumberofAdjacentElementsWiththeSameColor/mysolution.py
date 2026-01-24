class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = []
        ans = []
        for i in range(n):
            colors.append(0)
        for i, query in enumerate(queries):
            colors[query[0]] = query[1]
            ans.append(0)
            for j in range(n - 1):
                if colors[j] != 0 and colors[j] == colors[j + 1]:
                    ans[i] += 1
        return ans