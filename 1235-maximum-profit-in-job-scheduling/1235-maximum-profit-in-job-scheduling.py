class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        schedule = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        schedule.sort(key=lambda x: x[0])
        @cache
        def dp(i):
            if i >= n:
                return 0
            not_take = dp(i + 1)
            take = schedule[i][2]
            cur_end = schedule[i][1]
            j = bisect_left(schedule, cur_end, key=lambda x: x[0])
            return max(not_take, take + dp(j))
        return dp(0)