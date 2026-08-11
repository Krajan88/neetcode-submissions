class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = list(s)
        word1.sort()

        word2 = list(t)
        word2.sort()

        if word1 == word2:
            return True
        return False
    