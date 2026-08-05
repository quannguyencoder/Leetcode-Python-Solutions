class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_even = 0
        prefix_odd = 0
        suffix_even = 0
        suffix_odd = 0
        for i in range(n):
            if i % 2 == 0:
                suffix_even += nums[i]
                continue
            suffix_odd += nums[i]
        res = 0
        for i in range(n):
            if i % 2 == 0:
                suffix_even -= nums[i]
            else:
                suffix_odd -= nums[i]
            if suffix_even + prefix_odd == suffix_odd + prefix_even:
                res += 1
            if i % 2 == 0:
                prefix_even += nums[i]
                continue
            prefix_odd += nums[i]     
        return res