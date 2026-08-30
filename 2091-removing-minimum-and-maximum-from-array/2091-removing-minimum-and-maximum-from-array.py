class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 1:
            return 2
        n = len(nums)
        min_num, max_num = min(nums), max(nums)
        min_idx, max_idx = nums.index(min_num), nums.index(max_num)
        l, r = min(min_idx, max_idx), max(min_idx, max_idx)
        return min(r + 1, n - l, n + l + 1 - r)