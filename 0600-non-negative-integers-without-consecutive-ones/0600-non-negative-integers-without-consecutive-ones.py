from functools import cache
class Solution:
    def findIntegers(self, n: int) -> int:
        binary = bin(n)[2:]
        n_b = len(binary)
        @cache
        def digit_dp(idx, last, tight):
            if idx == n_b:
                return 1
            upper = int(binary[idx]) if tight else 1
            res = 0 
            for i in range(upper + 1):
                if last == 1 and i == 1:
                    continue
                new_tight = tight and (i == upper)
                res += digit_dp(idx + 1, i, new_tight)
            return res
        return digit_dp(0, 0, True)