class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        change = []
        for i in range(len(nums1)):
            change.append(nums1[i] - nums2[i])
        unique_vals = set()
        for val in change:
            unique_vals.add(val)
            unique_vals.add(val + diff)
        sorted_vals = sorted(list(unique_vals))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_vals)}

        n = len(sorted_vals)
        bit = [0] * (n + 1)
        def update(idx, val):
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
        def query(idx):
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total
        res = 0
        for i in range(len(change)):
            res += query(rank_map[change[i] + diff])
            update(rank_map[change[i]], 1)
        return res