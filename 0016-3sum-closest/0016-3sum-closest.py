class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        res = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r] + nums[i]
                cur_diff = abs(target - cur)
                if cur_diff == 0:
                    return cur
                if cur_diff < min_diff:
                    res = cur
                    min_diff = cur_diff
                if cur > target:
                    r -= 1
                else:
                    l += 1
        return res