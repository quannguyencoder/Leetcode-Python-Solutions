class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def update(i, delta):
            while i < len(fenwick):
                fenwick[i] += delta
                i += i & (-i)
        def query(i):
            total = 0
            while i > 0:
                total += fenwick[i]
                i -= i & (-i)
            return total
        seen = set(nums)
        for num in nums:
            seen.add(2 * num)
        sorted_num = sorted(list(seen))
        fenwick = [0] * (len(sorted_num) + 1)
        rank = {val: i + 1 for i, val in enumerate(sorted_num)}
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            cur_rank = rank[nums[i]]
            res += query(cur_rank - 1)
            time_2 = rank[2 * nums[i]]
            update(time_2, 1)

        return res