class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        colorDict = dict()
        ans = []
        for query in queries:
            colorDict[query[0]] = query[1]
            ans.append(len(set(colorDict.values())))
        return ans