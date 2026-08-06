class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        if not length:
            return -1
        elif nums[0] == target:
            return 0
        elif nums[length - 1] == target:
            return length - 1
        
        startPos = 0
        endPos = length - 1
        midPos = (startPos + endPos) // 2
        while startPos < length and endPos > 0 and endPos > startPos:
            print("startPos=", startPos, ", endPos=", endPos, ", midPos=", midPos)
            if nums[startPos] == target:
                return startPos
            elif nums[endPos] == target:
                return endPos
            
            midPos = (startPos + endPos) // 2
            if nums[midPos] == target:
                return midPos
            else:
                if nums[midPos] > nums[startPos]:
                    if nums[midPos] < target:
                        startPos = midPos
                    elif nums[midPos] > target and target > nums[startPos]:
                        endPos = midPos
                    elif nums[midPos] > target and target < nums[startPos]:
                        startPos = midPos
                elif nums[midPos] < nums[startPos]:
                    if nums[midPos] > target:
                        endPos = midPos
                    elif nums[midPos] < target and target > nums[startPos]:
                        endPos = midPos
                    elif nums[midPos] < target and target < nums[startPos]:
                        startPos = midPos
                else:
                    startPos = midPos + 1
        return -1
            