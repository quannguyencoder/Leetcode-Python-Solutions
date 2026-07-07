class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0] + nums
        self.n = len(nums)
        self.fenwick = [0] * (self.n + 1)
        for self.i in range(1, self.n + 1):
            self.upd(self.i, self.arr[self.i])
        
    def upd(self, idx: int, val: int) -> None:
        while idx <= self.n:
            self.fenwick[idx] += val
            idx += idx & (-idx)

    def update(self, index: int, val: int) -> None:
        self.change = val - self.arr[index + 1]
        self.arr[index + 1] = val
        self.upd(index + 1, self.change)
    def pre_i(self, i: int) -> int:
        self.total = 0
        while i > 0:
            self.total += self.fenwick[i]
            i -= i & (-i)
        return self.total
    def sumRange(self, left: int, right: int) -> int:
        return self.pre_i(right + 1) - self.pre_i(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)