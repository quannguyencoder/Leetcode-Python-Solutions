class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            max_num = min_num = nums[i]
            for j in range(i):
                max_num = max(nums[j], max_num)
            for j in range(i, len(nums)):
                min_num = min(nums[j], min_num)
            if abs(max_num - min_num) <= k:
                return i
        return -1