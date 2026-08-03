class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(val):
            cur_k = 1
            cur = 0
            for num in nums:
                cur += num
                if cur > val:
                    cur_k += 1
                    cur = num
            return cur_k <= k
        left = max(nums)
        right = sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res