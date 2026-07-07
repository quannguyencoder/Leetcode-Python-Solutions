class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = 10 ** 9
        pref_sum = [0] + list(accumulate(nums))
        queue = deque()
        for i in range(len(nums) + 1):
            while queue and pref_sum[i] - pref_sum[queue[0]] >= k:
                cur = i - queue[0]
                if cur < res:
                    res = cur
                queue.popleft()
            while queue and pref_sum[i] <= pref_sum[queue[-1]]:
                queue.pop()
            queue.append(i)

        return -1 if res == 10 ** 9 else res