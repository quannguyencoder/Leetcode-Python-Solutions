class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample_char = '123456789'
        max_n = 10
        res = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(max_n - length):
                cur_char = int(sample_char[start: start + length])
                if low <= cur_char <= high:
                    res.append(cur_char)
        return res