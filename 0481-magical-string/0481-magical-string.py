class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        seen = {'1': '2', '2': '1'}
        res = 1
        cur = '122'
        cur_point = '2'
        cur_length = 3
        left = 2
        while cur_length < n:
            cur_add = seen[cur_point] * int(cur[left])
            cnt_1 = min(n - cur_length, cur_add.count('1'))
            cur_length += int(cur[left])
            res += cnt_1
            cur += cur_add
            left += 1
            cur_point = seen[cur_point]
        return res