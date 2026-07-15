class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n ** 2
        sum_even = n * (n + 1)
        return gcd(sum_odd, sum_even)