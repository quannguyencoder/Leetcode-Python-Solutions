class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        last_position = [-1, -1, -1]
        for i, num in enumerate(s):
            if num == 'a':
                last_position[0] = i
            elif num == 'b':
                last_position[1] = i
            elif num == 'c':
                last_position[2] = i
            res += min(last_position) + 1
        return res