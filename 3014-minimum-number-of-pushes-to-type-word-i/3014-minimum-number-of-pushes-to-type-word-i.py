class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        times = n // 8
        return 8 * (times * (times + 1) // 2) + (n % 8) * (times + 1)