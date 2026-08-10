class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dp(n):
            if n == 0:
                return False
            for i in range(1, isqrt(n) + 1):
                if dp(n - (i ** 2)) == False:
                    return True
            return False
        return dp(n)