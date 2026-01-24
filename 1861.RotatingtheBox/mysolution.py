class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        ans = []
        rowLen = len(boxGrid[0])
        colLen = len(boxGrid)
        for i in range(rowLen):
            ans.append([])
        for i in range(colLen -1, -1, -1):
            bottom = rowLen - 1
            for j in range(rowLen - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    bottom = j - 1
                elif boxGrid[i][j] == '#':
                    temp = boxGrid[i][bottom]
                    boxGrid[i][bottom] = boxGrid[i][j]
                    boxGrid[i][j] = temp
                    if bottom != j:
                        ans[bottom][colLen - 1 - i] = '#'
                    bottom -= 1
                ans[j].append(boxGrid[i][j])
        return ans