import math
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        - Có n tầng
        - Có k quả trứng riêng biệt
        - Chắc chắn có 1 tầng đáp án
        - Tầng đáp án là tầng mà các tầng <= thả trứng ko vỡ, còn lớn hơn là vỡ
        - Nếu trứng vỡ thì vỡ luôn
        - Tìm số  bước thả ít nhất chắc chắn tìm ra tầng res
        - 1 <= k <= 100
        - 1 <= n <= 10^4
        """
        @cache
        def check(k, m):
            if k == 0 or m == 0:
                return 0
            return check(k - 1, m - 1) + check(k, m - 1) + 1
        l, r = 0, n
        res = n
        while l <= r:
            mid = (l + r) // 2
            if check(k, mid) >= n:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res