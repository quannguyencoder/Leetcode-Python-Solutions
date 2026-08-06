class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        product = [1] * 102
        for i in range(1, 101):
            product[i] = product[i // 10] * (i % 10)
        product[0] = 0
        for i in range(n, 101):
            if product[i] % t == 0:
                return i