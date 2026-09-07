class Solution(object):
    def distinctSubseqII(self, S):
        dp = [1]
        seen = {}
        for i in range(len(S)):
            cur = S[i]
            dp.append(dp[-1] * 2)
            if cur in seen:
                dp[-1] -= dp[seen[cur]]
            seen[cur] = i

        return (dp[-1] - 1) % (10**9 + 7)