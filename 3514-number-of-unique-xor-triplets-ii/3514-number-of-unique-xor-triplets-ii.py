class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniqeue_num = set(nums)
        cur = uniqeue_num
        for _ in range(2):
            res = set()
            for i in uniqeue_num:
                for j in cur:
                    res.add(i ^ j)
            cur = list(res)
        return len(res)