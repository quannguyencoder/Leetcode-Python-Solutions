import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return int(heapq.nlargest(k, nums)[-1])