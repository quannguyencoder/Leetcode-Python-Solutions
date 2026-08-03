class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dij = []
        heappush(dij, [0, 0, 0])
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        while dij:
            min_effort, x, y = heappop(dij)
            if (x, y) == (m - 1, n - 1):
                return min_effort
            if min_effort > efforts[x][y]:
                continue
            for curx, cury in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nextx, nexty = x + curx, y + cury
                if 0 <= nextx < m and 0 <= nexty < n:
                    change = max(min_effort, abs(heights[x][y] - heights[nextx][nexty]))
                    if change < efforts[nextx][nexty]:
                        heappush(dij, [change, nextx, nexty])
                        efforts[nextx][nexty] = change
