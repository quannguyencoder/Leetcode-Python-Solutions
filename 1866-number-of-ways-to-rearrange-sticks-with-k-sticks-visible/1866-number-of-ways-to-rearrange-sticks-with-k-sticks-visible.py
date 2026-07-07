class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dp(n: int, k: int):
            if n == k:
                return 1
            if n == 0:
                return 0
            return ((dp(n - 1, k - 1) % mod)  + ((n - 1) * dp(n - 1, k)) % mod) % mod
        return dp(n, k) % mod