class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        prod = 1
        for num in str(n):
            total += int(num)
            prod *= int(num)
        return n % (total + prod) == 0