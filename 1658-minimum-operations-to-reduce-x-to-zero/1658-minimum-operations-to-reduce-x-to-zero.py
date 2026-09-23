class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        cur = sum(A) - x
        if cur < 0: 
            return -1 
        res = -1
        s = i = 0
        for j in range(len(A)):
            s += A[j]
            while s > cur:
                s -= A[i]
                i += 1  
            if s == cur:
                res = max(res, j - i + 1)

        return -1 if res < 0 else len(A) - res
