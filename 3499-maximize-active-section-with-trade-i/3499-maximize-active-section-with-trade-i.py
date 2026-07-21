class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        nums = [0]
        for num in s:
            if num == '0':
                if nums[-1] < 0:
                    nums[-1] += -1
                else:
                    nums.append(-1)
            else:
                if nums[-1] > 0:
                    nums[-1] += 1
                else:
                    nums.append(1)
        nums = nums[1:]
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num) if num > 0 else prefix_sum.append(prefix_sum[-1])
        res = prefix_sum[-1]
        for i in range(1, len(nums) - 1):
            if nums[i] > 0:
                cur = abs(nums[i - 1]) + nums[i] + abs(nums[i + 1])
                suffix = prefix_sum[-1] - prefix_sum[i + 1]
                prefix = prefix_sum[i-1]
                res = max(res, cur + suffix + prefix)
        return res