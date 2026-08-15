class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if list(set(nums)) == [0]:
            return 0
        xor = 0
        for num in nums:
            xor ^= num
        if xor == 0:
            return len(nums) - 1
        return len(nums)