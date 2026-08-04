class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        bfs = deque([(0, entrance[0], entrance[1])])
        seen = {(entrance[0], entrance[1])}
        m, n = len(maze), len(maze[0])
        while bfs:
            time, row, column = bfs.popleft()
            if (row in (0, m - 1) or column in (0, n - 1)) and [row, column] != entrance:
                return time
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newx, newy = row + x, column + y
                if 0 <= newx < m and 0 <= newy < n and maze[newx][newy] == '.' and (newx, newy) not in seen:
                    seen.add((newx, newy))
                    bfs.append([time + 1, newx, newy])
        return -1
