class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = k
        for num in nums:
            if num == cur:
                cur += k
                
        return cur