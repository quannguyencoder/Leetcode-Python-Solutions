class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        zeros = [len(sub_0) for sub_0 in s.split('1') if sub_0]
        if len(zeros) < 2:
            return ones
        max_zeros = max(zeros[i] + zeros[i + 1] for i in range(len(zeros) - 1))
        return ones + max_zeros