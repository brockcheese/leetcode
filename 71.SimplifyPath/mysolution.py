class Solution:
    def simplifyPath(self, path: str) -> str:
        directorylist = []
        i = 0
        start = -1
        end = -1
        pathLen = len(path)
        for i in range(pathLen):
            if path[i] == '/':
                end = i - 1
                if end >= 0 and start >= 0 and end >= start:
                    directorylist.append(path[start:end+1])
                start = i + 1
        if start < pathLen:
            directorylist.append(path[start:pathLen])
        i = 0
        lenDirectorylist = len(directorylist)
        while i < lenDirectorylist:
            if directorylist[i] == '.':
                directorylist.pop(i)
                i -= 1
                lenDirectorylist -= 1
            if directorylist[i] == '..':
                if i - 1 > 0:
                    directorylist.pop(i)
                    directorylist.pop(i - 1)
                    i -= 2
                    lenDirectorylist -= 2
                else:
                    directorylist.pop(i)
                    i -= 1
                    lenDirectorylist -= 1
            i += 1
        ans = ""
        for directory in directorylist:
            ans += '/'
            ans += directory
        if ans == "":
            return '/'
        return ans