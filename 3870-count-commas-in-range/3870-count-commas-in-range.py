class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        for cur in range(1, n + 1):
            if cur > 999:
                res += 1
        return res