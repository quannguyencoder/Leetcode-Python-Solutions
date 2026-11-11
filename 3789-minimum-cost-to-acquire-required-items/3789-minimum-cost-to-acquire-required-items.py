class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res = 0
        min_cost = min(costBoth, cost1 + cost2)
        min_both = min(need1, need2)
        res += min_cost * min_both
        rem_1 = need1 - min_both
        rem_2 = need2 - min_both
        min_1 = min(costBoth, cost1)
        min_2 = min(costBoth, cost2)
        res += rem_1 * min_1
        res += rem_2 * min_2
        return res