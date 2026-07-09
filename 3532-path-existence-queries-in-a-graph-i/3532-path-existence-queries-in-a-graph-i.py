import gc
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        gc.disable()
        parent = [i for i in range(n)]
        size = [1] * n
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return
            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u
            parent[root_v] = root_u
            size[root_u] += size[root_v]
            
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for i in range(n - 1):
            if abs(nums[i + 1] - nums[i]) <= maxDiff:
                union(i + 1, i)
        res = []
        for i in range(len(queries)):
            u, v = queries[i]
            if find(u) == find(v):
                res.append(True)
                continue
            res.append(False)
        return res