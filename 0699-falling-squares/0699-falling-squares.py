class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        cords = set()
        for left, side in positions:
            cords.add(left)
            cords.add(left + side - 1)
        sorted_cord = sorted(list(cords))
        rank = {val: i + 1 for i, val in enumerate(sorted_cord)}
        m = len(sorted_cord)
        segment = [0] * (4 * m + 1)
        lazy = [0] * (4 * m + 1)
        def push(idx):
            if lazy[idx] != 0:
                segment[idx * 2] = lazy[idx]
                lazy[idx * 2] = lazy[idx]
                segment[idx * 2 + 1] = lazy[idx]
                lazy[idx * 2 + 1] = lazy[idx]
                lazy[idx] = 0
        def update(idx, l, r, u, v, val):
            if v < l or u > r:
                return
            if u <= l and r <= v:
                segment[idx] = val
                lazy[idx] = val
                return
            push(idx)
            mid = (l + r) // 2
            update(idx * 2, l, mid, u, v, val)
            update(idx * 2 + 1, mid + 1, r, u, v, val)
            segment[idx] = max(segment[idx * 2], segment[idx * 2 + 1])
            return 
        def query(idx, l, r, u, v):
            if v < l or u > r:
                return 0
            if u <= l and r <= v:
                return segment[idx]
            mid = (l + r) // 2
            push(idx)
            ans_left = query(idx * 2, l, mid, u, v)
            ans_right = query(idx *2 + 1, mid + 1, r, u, v)
            return max(ans_left, ans_right)
        ans = []
        for left, side in positions:
            right = left + side - 1
            idx_left = rank[left]
            idx_right = rank[right]
            base_height = query(1, 1, m, idx_left, idx_right)
            cur_height = base_height + side
            update(1, 1, m, idx_left, idx_right, cur_height)
            ans.append(segment[1])
        return ans
