class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        visited = {(0, 0)}
        heap = [(matrix[0][0], 0, 0)]
        n = len(matrix)
        for _ in range(k - 1):
            val, x, y = heappop(heap)
            if y + 1 < n and (x, y + 1) not in visited:
                heappush(heap, (matrix[x][y + 1], x, y + 1))
                visited.add((x, y + 1))
            if x + 1 < n and (x + 1, y) not in visited:
                heappush(heap, (matrix[x + 1][y], x + 1, y))
                visited.add((x + 1, y))
        return heappop(heap)[0]