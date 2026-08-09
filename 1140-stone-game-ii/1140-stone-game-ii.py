from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dp(i, m):
            if i >= len(piles):
                return 0
            if i + 2 * m >= len(piles):
                return sum(piles[i:])
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, sum(piles[i:]) - dp(i + x, max(m, x)))
            return res
        return dp(0, 1)