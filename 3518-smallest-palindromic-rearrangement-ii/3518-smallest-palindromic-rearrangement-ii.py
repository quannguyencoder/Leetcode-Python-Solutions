class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        mid = n // 2
        char = sorted(list(s[:mid]))
        k -= 1 
        first = []
        seen = Counter(char)
        cnt_factorial = math.factorial(mid)
        for c in seen.values():
            cnt_factorial //= math.factorial(c)
        if k >= cnt_factorial:
            return ''
        first = []
        L = mid
        while L > 0:
            for c in seen:
                if seen[c] > 0:
                    block = cnt_factorial * seen[c] // L
                    if k < block:
                        first.append(c)
                        seen[c] -= 1
                        cnt_factorial = block
                        L -= 1
                        break
                    else:
                        k -= block
                    
        middle = [s[mid]] if n % 2 == 1 else []
        return ''.join(first + middle + first[::-1])
        # n = len(s)
        # mid = n // 2
        # char = sorted(list(s[:mid]))
        # k -= 1
        # first = []
        # for i in range(mid - 1, -1, -1):
        #     cur_block = math.factorial(i)
        #     print(cur_block)
        #     idx = k // cur_block
        #     if idx >= len(char):
        #         return ''
        #     first.append(char.pop(idx))
        #     k %= cur_block
        # middle = [s[mid]] if n % 2 == 1 else []
        # return ''.join(first + middle + first[::-1])
        
"""
from collections import Counter
from functools import cache
import math


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)

        forMid = []
        sideCount = {}
        for char in sorted(counts.keys()):
            if counts[char] % 2 == 1:
                forMid.append(char)
            if counts[char] // 2 > 0:
                sideCount[char] = counts[char] // 2

        if len(forMid) > 1:
            return ""
        midChar = forMid[0] if forMid else ""

        @cache
        def getFactorial(n):
            return math.factorial(n)

        totalLen = sum(sideCount.values())

        def getTotalWays(countMap, totalN):
            res = getFactorial(totalN)
            for c in countMap.values():
                if c > 1:
                    res //= getFactorial(c)
            return res

        currentWays = getTotalWays(sideCount, totalLen)

        if k > currentWays:
            return ""

        side = []
        currLen = totalLen

        for _ in range(totalLen):
            for char in sorted(sideCount.keys()):
                charCount = sideCount[char]
                if charCount > 0:
                    ways = (currentWays * charCount) // currLen

                    if k <= ways:
                        side.append(char)
                        sideCount[char] -= 1
                        currentWays = ways
                        currLen -= 1
                        break
                    else:
                        k -= ways

        prefix = "".join(side)
        return prefix + midChar + prefix[::-1]
"""