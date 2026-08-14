class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = r = 0
        seen = {}
        res = float('-inf')
        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while seen[s[r]] > 2:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res