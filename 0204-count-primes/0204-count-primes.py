class Solution:
    def countPrimes(self, n: int) -> int:
        pref_sum = [0] * (n + 1)
        cnt = 0
        sieve = bytearray([1]) * (n + 1)
        if n > 2:
            sieve[2] = 1
            cnt += 1
            sieve[0] = sieve[1] = 0
            sieve[4: n: 2] = bytearray([0]) * len(sieve[4: n: 2])
            for i in range(3, n, 2):
                if sieve[i]:
                    cnt += 1
                    sieve[i * i: n: i * 2] = bytearray([0]) * len(sieve[i * i: n: i * 2])
        return cnt