class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        res = 1
        while res <= n:
            res *= 2
            print(res)
        return res