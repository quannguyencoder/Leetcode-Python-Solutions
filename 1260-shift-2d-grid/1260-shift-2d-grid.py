class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        res = copy.deepcopy(grid)
        for _ in range(k):
            res = copy.deepcopy(grid)
            for i in range(n):
                for j in range(m):
                    new_j = (j + 1) % m
                    new_i = (i + (j + 1) // m) % n
                    res[new_i][new_j] = grid[i][j]
            grid = copy.deepcopy(res)
        return res