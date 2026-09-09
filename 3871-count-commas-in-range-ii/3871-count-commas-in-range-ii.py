class Solution:
    def countCommas(self, n: int) -> int:
        cur = 1000
        res = 0
        while cur <= n:
            res += n - cur + 1
            cur *= 1000
        return res