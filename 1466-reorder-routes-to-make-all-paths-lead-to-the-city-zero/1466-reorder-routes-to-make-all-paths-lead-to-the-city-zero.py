class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(all_connect, visited, from_city):
            res = 0
            visited[from_city] = True
            for city in all_connect[from_city]:
                if visited[abs(city)] != True:
                    res += dfs(all_connect, visited, abs(city)) + (1 if city > 0 else 0)
            return res
        all_connect = [[] for _ in range(n)]
        visited = [False] * n
        for f_city, t_city in connections:
            all_connect[f_city].append(t_city)
            all_connect[t_city].append(-f_city)
        return dfs(all_connect, visited, 0)