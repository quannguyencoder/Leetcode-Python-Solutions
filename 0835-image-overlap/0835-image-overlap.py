class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        nums1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        nums2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        cnt = [[0] * (2 * n) for _ in range(2 * n)]
        res = 0
        for ax, ay in nums1:
            for bx, by in nums2:
                dx = bx - ax + n
                dy = by - ay + n
                cnt[dx][dy] += 1
                res = max(res, cnt[dx][dy])
        return res