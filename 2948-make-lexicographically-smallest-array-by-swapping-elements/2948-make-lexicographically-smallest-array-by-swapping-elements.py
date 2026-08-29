class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        ans = [0] * n

        start = 0
        for k in range(1, n + 1):
            if k == n or nums[order[k]] - nums[order[k - 1]] > limit:
                idx_sorted = sorted(order[start:k])      
                for idx, i in zip(idx_sorted, order[start:k]):
                    ans[idx] = nums[i]                    
                start = k

        return ans