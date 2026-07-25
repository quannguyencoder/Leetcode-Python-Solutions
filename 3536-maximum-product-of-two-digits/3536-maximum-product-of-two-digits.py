class Solution:
    def maxProduct(self, n: int) -> int:
        nums = sorted(list(map(int, str(n))), reverse=True)
        return nums[0] * nums[1]