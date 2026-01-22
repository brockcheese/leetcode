class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        myDict = dict()
        for n in arr:
            if n in myDict.keys():
                myDict[n] += 1
            else:
                myDict[n] = 1
        sortedDict = sorted(myDict.keys())
        for n in sortedDict:
            for i in range(0, myDict[n]):
                if n > 0:
                    double = n * 2
                elif n < 0:
                    double = n // 2
                if double not in myDict.keys():
                    return False
                else:
                    if myDict[double] > 0:
                        myDict[double] -= 1
                    else:
                        return False
        return True