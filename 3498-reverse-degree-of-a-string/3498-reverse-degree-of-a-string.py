class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            ch = s[i]
            res += (26 - (ord(ch) - ord("a"))) * (i + 1)
        return res