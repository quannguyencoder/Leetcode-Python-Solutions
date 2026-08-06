class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                cur += 1
            res += cur
        return res