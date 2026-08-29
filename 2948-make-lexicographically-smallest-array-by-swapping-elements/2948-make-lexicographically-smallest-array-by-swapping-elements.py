class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        # --- DSU inline bằng list + closure, không tạo class riêng ---
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]   # path compression (halving)
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # --- Bước A: sort chỉ số gốc theo giá trị nums[i] ---
        order = sorted(range(n), key=lambda i: nums[i])

        # --- Bước B: union các cặp liền kề trong order nếu thỏa điều kiện ---
        for k in range(1, n):
            i, j = order[k - 1], order[k]
            if nums[j] - nums[i] <= limit:
                union(i, j)

        # --- Bước C: gom các chỉ số gốc theo nhóm liên thông (root) ---
        groups: dict[int, list[int]] = {}
        for i in range(n):
            r = find(i)
            groups.setdefault(r, []).append(i)

        # --- Bước D: với mỗi nhóm, gán giá trị nhỏ nhất cho chỉ số nhỏ nhất ---
        ans = [0] * n
        for indices in groups.values():
            sorted_indices = sorted(indices)
            sorted_values = sorted(nums[i] for i in indices)
            for idx, val in zip(sorted_indices, sorted_values):
                ans[idx] = val

        return ans