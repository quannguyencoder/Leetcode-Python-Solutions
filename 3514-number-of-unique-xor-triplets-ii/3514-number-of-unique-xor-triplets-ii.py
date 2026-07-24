class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniqeue_num = list(set(nums))
        cur = uniqeue_num[:]
        for _ in range(2):
            res = set()
            for i in range(len(uniqeue_num)):
                for j in range(len(cur)):
                    res.add(uniqeue_num[i] ^ cur[j])
            cur = list(res)
        return len(res)