class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            odds = odds = [2 * num - 1 for num in res]
            evens = [2 * num for num in res]
            res = odds + evens
        return  [num for num in res if num <= n]