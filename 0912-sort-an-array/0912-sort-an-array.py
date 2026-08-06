class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(l, r):
            if l == r:
                return [nums[l]]
            mid = (l + r) // 2
            return merge(divide(l, mid), divide(mid + 1, r))
        def merge(l, r):
            res = []
            i = j = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1
            res.extend(l[i:])
            res.extend(r[j:])
            return res
        return divide(0, len(nums) - 1)