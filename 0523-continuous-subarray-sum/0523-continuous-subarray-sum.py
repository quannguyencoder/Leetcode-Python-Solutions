class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_total = 0
        prefix_mod = {0: -1}
        for i in range(len(nums)):
            cur_total += nums[i]
            cur_mod = cur_total % k
            if cur_mod in prefix_mod:
                if i - prefix_mod[cur_mod] > 1:
                    return True
            else:
                prefix_mod[cur_mod] = i
        return False