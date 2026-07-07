class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        total = 0
        for c in str(n):
            dig = int(c)
            total += dig
            if dig > 0:
                x = x * 10 + dig
        return x * total