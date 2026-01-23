class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        yDict = dict({0: 0, 1: 0, 2: 0})
        notYDict = dict({0: 0, 1: 0, 2: 0})
        gridLen = len(grid)
        half = gridLen // 2
        for i in range(gridLen):
            for j in range(gridLen):
                if i <= half:
                    if i == j or gridLen - 1 - j == i:
                        yDict[grid[i][j]] += 1
                    else:
                        notYDict[grid[i][j]] += 1
                else:
                    if j == half:
                        yDict[grid[i][j]] += 1
                    else:
                        notYDict[grid[i][j]] += 1
        inPlace = 0
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                combo = yDict[i] + notYDict[j]
                if combo > inPlace:
                    inPlace = combo
        return (gridLen * gridLen) - inPlace 

                    