class Solution:
    def maxProduct(self, n: int) -> int:
        digit = list(map(int, list(str(n))))
        num1 = max(digit)
        del digit[digit.index(num1)]
        num2 = max(digit)
        return num1 * num2