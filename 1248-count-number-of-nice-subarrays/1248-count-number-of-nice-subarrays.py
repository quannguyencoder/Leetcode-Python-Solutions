class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        cur = 0
        res = 0
        even_prefix = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                cur += 1
            while cur > k:
                if nums[left] % 2 != 0:
                    cur -= 1
                left += 1
                even_prefix = 0
            while cur == k and nums[left] % 2 == 0:
                even_prefix += 1
                left += 1
            if cur == k:
                res += 1 + even_prefix
        return res