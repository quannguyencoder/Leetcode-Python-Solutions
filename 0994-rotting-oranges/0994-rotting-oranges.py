class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = deque()
        seen = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs.append([0, i, j])
                    seen.add((i, j))
        time = 0
        while bfs:
            time, row, column = bfs.popleft()
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newx, newy = row + x, column + y
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1 and (newx, newy) not in seen:
                    seen.add((newx, newy))
                    bfs.append([time + 1, newx, newy])
                    grid[newx][newy] = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time
