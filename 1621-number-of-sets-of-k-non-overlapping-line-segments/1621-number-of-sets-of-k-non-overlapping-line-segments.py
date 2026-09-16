class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = (10 ** 9 + 7)
        return math.comb(n - 1 + k, k * 2) % MOD