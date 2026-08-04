class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for i in range(len(equations)):
            u, v = equations[i]
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        def dfs(start, end, visit):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1.0
            visit.add(start)
            for nex, val in graph[start].items():
                if nex not in visit:
                    cur_res = dfs(nex, end, visit)
                    if cur_res != -1.0:
                        return val * cur_res
            return -1.0
        res = []
        for u, v in queries:
            res.append(dfs(u, v, set()))
        return res