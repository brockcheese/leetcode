class Solution:
    def slideLeft(self, img1: list[list[int]]):
        ans = []
        for i in range(0, len(img1)):
            ans.append([])
            length = len(img1[i])
            for j in range(0, length):
                if j < length - 1:
                    ans[i].append(img1[i][j + 1])
                else:
                    ans[i].append(0)
        return ans
    
    def slideRight(self, img1: list[list[int]]):
        ans = []
        for i in range(0, len(img1)):
            ans.append([])
            length = len(img1[i])
            for j in range(0, length):
                if j == 0:
                    ans[i].append(0)
                else:
                    ans[i].append(img1[i][j - 1])
        return ans

    def slideUp(self, img1: list[list[int]]):
        ans = []
        length = len(img1)
        for i in range(0, length):
            ans.append([])
            for j in range(0, len(img1[i])):
                if i == length - 1:
                    ans[i].append(0)
                else:
                    ans[i].append(img1[i + 1][j])
        return ans

    def slideDown(self, img1: list[list[int]]):
        ans = []
        length = len(img1)
        for i in range(0, length):
            ans.append([])
            for j in range(0, len(img1[i])):
                if i == 0:
                    ans[i].append(0)
                else:
                    ans[i].append(img1[i - 1][j])
        return ans

    def calcOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        ans = 0
        allZero = True
        for i in range(0, len(img1)):
            for j in range(0, len(img1[i])):
                if img1[i][j] == 1:
                    allZero = False
                    if img2[i][j] == 1:
                        ans += 1
        if allZero == True:
            return -1
        return ans
    
    def calcMaximum(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        total1 = 0
        total2 = 0
        for i in range(0, len(img1)):
            for j in range(0, len(img1[i])):
                if img1[i][j] == 1:
                    total1 += 1
                if img2[i][j] == 1:
                    total2 += 1
        if total2 < total1:
            return total2
        return total1

    def largestOverlapHelper(self, img1: list[list[int]], img2: list[list[int]], maximum: int, direction: int) -> int:
        overlap = self.calcOverlap(img1, img2)
        if overlap == -1:
            return 0
        if overlap == maximum:
            return overlap

        if direction not in range(3, 6):
            left = self.slideLeft(img1)
            if direction == 2:
                leftdirection = 1
            elif direction == 0:
                leftdirection = 8
            else:
                leftdirection = 7
            temp = self.largestOverlapHelper(left, img2, maximum, leftdirection)
            if temp > overlap:
                overlap = temp
            if overlap == maximum:
                return overlap

        if direction not in range(7, 9) and direction != 1:
            right = self.slideRight(img1)
            if direction == 2:
                rightdirection = 3
            elif direction == 0:
                rightdirection = 4
            else:
                rightdirection = 5
            temp = self.largestOverlapHelper(right, img2, maximum, rightdirection)
            if temp > overlap:
                overlap = temp
            if overlap == maximum:
                return overlap

        if direction not in range(5, 8):
            up = self.slideUp(img1)
            if direction == 8:
                updirection = 1
            elif direction == 0:
                updirection = 2
            else:
                updirection = 3
            temp = self.largestOverlapHelper(up, img2, maximum, updirection)
            if temp > overlap:
                overlap = temp
            if overlap == maximum:
                return overlap

        if direction not in range(1, 4):
            down = self.slideDown(img1)
            if direction == 8:
                downdirection = 7
            elif direction == 0:
                downdirection = 6
            else:
                downdirection = 5
            temp = self.largestOverlapHelper(down, img2, maximum, downdirection)
            if temp > overlap:
                overlap = temp
        return overlap

    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        maximum = self.calcMaximum(img1, img2)
        if maximum < 2:
            return maximum
        ans = self.largestOverlapHelper(img1, img2, maximum, 0)
        return ans