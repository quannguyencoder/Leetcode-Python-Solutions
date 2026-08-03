class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dp(i):
            if i >= len(stoneValue):
                return 0
            cur = stoneValue[i] - dp(i + 1)
            if i + 1 < len(stoneValue):
                cur = max(cur, stoneValue[i] + stoneValue[i + 1] - dp(i + 2))
            if i + 2 < len(stoneValue):
                cur = max(cur, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp(i + 3))
            return cur
        res = dp(0)
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        return 'Tie'