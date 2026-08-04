class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        connect = 0
        n = len(isConnected)
        def dfs(city):
            visited.add(city)
            for nex in range(n):
                if isConnected[city][nex] == 1 and nex not in visited:
                    dfs(nex)
        for i in range(n):
            if i not in visited:
                connect += 1
                dfs(i)
        return connect
