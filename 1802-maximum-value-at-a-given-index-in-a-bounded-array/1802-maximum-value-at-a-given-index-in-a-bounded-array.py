class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def cal(peak, length):
            if peak < length:
                return (peak * (peak + 1) // 2) + (length - peak)
            return (peak + (peak - length + 1)) * length // 2
        left = 1
        right = maxSum
        res = 0
        while left <= right:
            target = (left + right) // 2
            start_len = index
            end_len = n - index - 1
            check = target + cal(target - 1, start_len) + cal(target - 1, end_len)
            if check > maxSum:
                right = target - 1
            else:
                res = max(res, target)
                left = target + 1
        return res