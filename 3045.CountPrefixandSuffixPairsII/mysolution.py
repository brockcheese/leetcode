class Solution:
    def isPrefixAndSuffix(self, word1: str, word2: str) -> bool:
        word1len = len(word1)
        word2len = len(word2)
        if len(word1) > len(word2):
            return False
        if word1 in word2[0:word1len] and word1 in word2[word2len - word1len:word2len]:
            return True
        return False

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans