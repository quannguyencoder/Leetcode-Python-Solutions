class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left = 0
        right = n - 1
        while left < n and right >= 0:
            left_max[left] = max(height[left], left_max[max(left - 1, 0)])
            right_max[right] = max(height[right], right_max[min(right + 1, n - 1)])
            left += 1
            right -= 1

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res