class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freg = 0
        seen = {}
        left = 0
        res = float('-inf')
        for right in range(len(s)):
            new_add = s[right]
            seen[new_add] = seen.get(new_add, 0) + 1
            max_freg = max(max_freg, seen[new_add])
            cur_length = right - left + 1
            if cur_length - max_freg > k:
                left += 1
                seen[s[left - 1]] -= 1
            res = max(res, right - left + 1)
        return res