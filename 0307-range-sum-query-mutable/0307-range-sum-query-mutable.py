class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = [0] + nums
        self.n = len(nums)
        self.fenwick = [0] * (self.n + 1)
        
        for i in range(1, self.n + 1):
            self.upd(i, self.arr[i])
        
    def upd(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.fenwick[idx] += delta
            idx += idx & (-idx)

    def update(self, index: int, val: int) -> None:
        change = val - self.arr[index + 1]
        self.arr[index + 1] = val
        self.upd(index + 1, change)
        
    def pre_i(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.fenwick[i]
            i -= i & (-i)
        return total
        
    def sumRange(self, left: int, right: int) -> int:
        return self.pre_i(right + 1) - self.pre_i(left)