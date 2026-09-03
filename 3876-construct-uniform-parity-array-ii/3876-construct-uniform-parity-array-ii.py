class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        num = nums1[0]
        odd = False
        for cur in nums1:
            if cur < num:
                num = cur
            if cur & 1:
                odd = True
        if num & 1:
            return True
        return not odd