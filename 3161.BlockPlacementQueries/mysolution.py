class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        obstacles = set()
        ans = []
        for query in queries:
            if query[0] == 1:
                obstacles.add(query[1])
            else:
                n = 0
                m = 0
                numObstacles = 0
                for i in range(1, query[2]):
                    m += 1
                    if m in obstacles:
                        numObstacles += 1
                while m < query[1] - 1 and numObstacles > 0:
                    n += 1
                    m += 1
                    if m in obstacles:
                        numObstacles += 1
                    if n in obstacles:
                        numObstacles -= 1
                if numObstacles > 0:
                    ans.append(False)
                else:
                    ans.append(True)
        return ans