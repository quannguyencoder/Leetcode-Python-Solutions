class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        pre = [0] + list(accumulate(nums))
        total = []
        for k in range(l, r + 1):
            for i in range(len(pre) - k):
                total.append(pre[i + k] - pre[i])
        return min((s for s in total if s > 0), default = -1)