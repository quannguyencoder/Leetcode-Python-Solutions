class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = list(accumulate(stones))
        dp = [0] * n
        dp[n - 1] = pre[n - 1]
        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], pre[i] - dp[i + 1])
        return dp[1]