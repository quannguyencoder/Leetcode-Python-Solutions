class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        check = [[nums1[i], nums2[i]] for i in range(len(nums1))]
        check.sort(key=lambda x: x[1], reverse = True)

        min_heap = []
        cur = 0
        res = 0

        for num, point in check:
            cur += num
            heappush(min_heap, num)

            if len(min_heap) > k:
                cur -= heappop(min_heap)

            if len(min_heap) == k:
                res = max(res, cur * point)
        return res