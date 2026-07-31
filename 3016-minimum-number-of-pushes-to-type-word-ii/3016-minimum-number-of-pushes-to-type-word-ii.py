class Solution:
    def minimumPushes(self, word: str) -> int:
        cnts = list(Counter(word).items())
        cnts.sort(key=lambda x: -x[1])
        res = 0
        for i, char_times in enumerate(cnts):
            res += (i // 8 + 1) * char_times[1]
        return res