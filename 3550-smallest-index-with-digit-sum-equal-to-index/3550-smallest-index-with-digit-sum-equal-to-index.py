class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        LIMIT = 1001
        sum_digit = [0] * LIMIT
        for i in range(1, 1001):
            sum_digit[i] = sum_digit[i // 10] + (i % 10)
        for i in range(len(nums)):
            if i == sum_digit[nums[i]]:
                return i
        return -1