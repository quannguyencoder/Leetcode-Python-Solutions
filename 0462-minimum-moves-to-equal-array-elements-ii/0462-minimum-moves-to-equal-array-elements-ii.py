class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mean = nums[n // 2]
        ans = 0
        for num in nums:
            ans += abs(mean - num)
        return ans