class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        cur_total = nums[0]
        for i in range(1, len(nums)):
            cur_total += nums[i]
            if nums[i - 1] + 1 != nums[i]:
                cur_total -= nums[i]
                break
        for num in range(cur_total, (cur_total + 50) * 50):
            if num not in nums:
                return num