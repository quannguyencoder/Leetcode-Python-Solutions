from functools import lru_cache, cache
from math import gcd

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for i in range(2, 8):
            while temp % i == 0:
                temp //= i
        if temp > 1:
            return "-1"
        n = len(num)
        @cache
        def another_dp(length, cur_rem):
            if length == 0:
                return '' if cur_rem == 1 else None
            if length > 50:
                suffix = another_dp(50, cur_rem)
                if suffix is not None:
                    return '1' * (length - 50) + suffix
                return None
            for i in range(1, 10):
                new_rem = cur_rem // gcd(cur_rem, i)
                cur_res = another_dp(length - 1, new_rem)
                if cur_res is not None:
                    return str(i) + cur_res
            return None
        def dp(i, is_limit, rem):
            if i == n:
                return '' if rem == 1 else None
            if not is_limit:
                return another_dp(n - i, rem)
            cur_up = 1 if not is_limit else max(1, int(num[i]))
            for cur_num in range(cur_up, 10):
                new_limit = is_limit and cur_num == int(num[i])
                new_rem = rem // gcd(rem, cur_num)
                cur_res = dp(i + 1, new_limit, new_rem)
                if cur_res is not None:
                    return str(cur_num) + cur_res
            return None
        res = dp(0, True, t)
        if res:
            return res
        cur_length = n + 1
        while True:
            res = another_dp(cur_length, t)
            if res is not None:
                return res
            cur_length += 1
    
        