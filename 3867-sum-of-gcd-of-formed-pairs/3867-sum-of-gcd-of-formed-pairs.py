class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        cur_max = nums[0]
        prefix = []
        n = len(nums)
        for i in range(n):
            cur_max = max(nums[i], cur_max)
            prefix.append(gcd(cur_max, nums[i]))
        prefix.sort()
        res = 0
        for i in range(n // 2):
            right = n - 1 - i
            res += gcd(prefix[i], prefix[right])
        return res