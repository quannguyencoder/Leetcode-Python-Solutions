class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_max = []
        for i in range(len(nums)):
            if i == 0:
                prefix_max.append(nums[i])
            else:
                prefix_max.append(max(prefix_max[i-1],nums[i]))
        suffix_min = [0] * len(nums)
        suffix_min[-1] = nums[i]
        for i in range(len(nums)-2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        for i in range(len(nums)):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        return -1