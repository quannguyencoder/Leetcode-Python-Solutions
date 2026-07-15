class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_even = n * (n + 1)
        sum_odd = n ** 2
        return gcd(sum_even, sum_odd)