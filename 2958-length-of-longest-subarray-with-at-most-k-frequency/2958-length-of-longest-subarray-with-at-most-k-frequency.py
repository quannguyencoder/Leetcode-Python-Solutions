class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = r = 0
        res = k
        seen = {}
        while r < len(nums):
            seen[nums[r]] = seen.get(nums[r], 0) + 1
            while seen[nums[r]] > k:
                seen[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res