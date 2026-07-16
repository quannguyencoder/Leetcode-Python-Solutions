from functools import cmp_to_key
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def check(num1, num2):
            x1, y1 = num1
            x2, y2 = num2
            cur1 = x1 ** 2 + y1 ** 2
            cur2 = x2 ** 2 + y2 ** 2
            if cur1 < cur2:
                return -1
            elif cur1 > cur2:
                return 1
            return 0
        points.sort(key=cmp_to_key(check))
        return points[:k]