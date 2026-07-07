class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(list(set(nums)))
        n = len(arr)
        rank = {val: i + 1 for i, val in enumerate(arr)}
        n_nums = len(nums)
        bit = [0] * (n + 1)
        def update(i: int, val: int):
            while i <= n:
                bit[i] += val
                i += i & (-i)
        def query(i: int):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & (-i)
            return total
        res = [0] * n_nums
        for i in range(n_nums - 1, -1, -1):
            num = nums[i]
            index = rank[num]
            res[i] = query(index - 1)
            update(index, 1)
        return res