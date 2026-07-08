class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        return self.pref_sum[n - 1]
    N = 5 * pow(10, 6) + 1
    sieve = [1] * (N + 1)
    sieve[0] = sieve[1] = 0
    sieve[4: N: 2] = [0] * len(sieve[4: N: 2])
    for i in range(3, isqrt(N), 2):
        if sieve[i]:
            sieve[i * i: N: i * 2] = [0] * len(sieve[i * i: N: i * 2])
    pref_sum = list(accumulate(sieve))