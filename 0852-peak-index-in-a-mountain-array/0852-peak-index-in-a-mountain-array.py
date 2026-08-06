class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            nextNum = arr[mid + 1]
            if arr[mid] > nextNum and arr[mid - 1] < arr[mid]:
                return mid
            if arr[mid] < nextNum:
                l = mid + 1
            else:
                r = mid - 1
        return l