class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suffix = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suffix[i] = suffix[i + 1] + 1
                j -= 1
            else:
                suffix[i] = suffix[i + 1]
        
        res = []
        i = j = 0
        ticket = 1
        while i < n and j < m:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            else:
                length_af = m - j - 1
                if ticket > 0 and suffix[i + 1] >= length_af:
                    res.append(i)
                    j += 1
                    ticket -= 1
            i += 1
        return res if m == len(res) else []