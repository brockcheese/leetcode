class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        i = -1
        testans = []
        teststr = ""
        for word in words:
            if len(teststr + word) >= maxWidth:
                i += 1
                ans.append("")
                space = maxWidth - len(teststr) + len(testans) - 1
                if (len(testans) > 1):
                    mod = space % (len(testans) - 1)
                    space //= len(testans) - 1
                for w in testans:
                    if not ans[i]:
                        ans[i] += w
                        if len(testans) == 1:
                            ans[i] += ' ' * (maxWidth - len(ans[i]))
                    else:
                        if mod > 0:
                            ans[i] += ' '
                            mod -= 1
                        ans[i] += (' ' * space) + w
                teststr = ""
                testans = []
            if not teststr:
                teststr += word
            else:
                teststr += ' ' + word
            testans.append(word)
        i += 1
        ans.append("")
        for w in testans:
            if not ans[i]:
                ans[i] += w
            else:
                ans[i] += ' ' + w
        ans[i] += ' ' * (maxWidth - len(ans[i]))
        return ans
                