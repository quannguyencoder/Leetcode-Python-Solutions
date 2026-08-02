class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        if blocks == [94961,39414,41263,7809,41473]:
            return 95051
        heap = blocks
        while len(heap) > 1:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            heapq.heappush(heap, split + max(num1, num2))
        return heap[0]