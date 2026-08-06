class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = isqrt(c)
        while start <= end:
            cur = start ** 2 + end ** 2 
            if cur == c:
                return True
            if cur > c:
                end -= 1
            else:
                start += 1
        return False