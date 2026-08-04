class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], (-x[1])))
        heights = [height for x, height in envelopes]
        tails = []
        for num in heights:
            idx = bisect.bisect_left(tails, num)
            if idx >= len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)