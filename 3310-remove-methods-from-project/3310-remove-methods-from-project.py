class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        suspicious = set()
        grid = [[] for _ in range(n)]
        for u, v in invocations:
            grid[u].append(v)
        @cache
        def dfs(cur):
            suspicious.add(cur)
            for f1 in grid[cur]:
                if f1 not in suspicious:
                    dfs(f1)
        dfs(k)
        clean = []
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return [i for i in range(n)]
        for i in range(n):
            if i not in suspicious:
                clean.append(i)
        return clean