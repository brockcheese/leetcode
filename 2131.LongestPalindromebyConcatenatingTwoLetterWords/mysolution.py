class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        ans = dict()
        ans["center"] = dict()
        for word in words:
            if word[0] == word[1]:
                if word in ans["center"].keys():
                    ans["center"][word] += 1
                else:
                    ans["center"][word] = 1
            elif word[::-1] in ans.keys() and ans[word[::-1]] == None:
                ans[word[::-1]] = word
            else:
                ans[word] = None
        ret = 0
        for key in ans.keys():
            if key != "center" and ans[key] != None:
                ret += 4
        maxCenter = 0
        for center in ans["center"].keys():
            if ans["center"][center] > maxCenter:
                maxCenter = ans["center"][center]
        ret += maxCenter * 2
        return ret