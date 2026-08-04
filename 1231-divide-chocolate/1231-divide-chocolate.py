class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(min_point: int) -> bool:
            print(min_point)
            cur = 0
            cnt = 1
            for num in sweetness:
                cur += num
                if cur >= min_point:
                    cur = 0
                    cnt += 1
            print(cnt)
            print(cnt > k + 1)
            return cnt > k + 1
        l, r = min(sweetness), sum(sweetness)
        res = l
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
