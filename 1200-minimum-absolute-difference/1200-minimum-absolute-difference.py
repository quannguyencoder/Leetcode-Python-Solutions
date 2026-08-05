class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minimum_dif = float('inf')
        n = len(arr)
        arr.sort()
        answer = []
        for i in range(1, n):
            minimum_dif = min(arr[i] - arr[i - 1], minimum_dif)
        for i in range (1, n):
            if arr[i] - arr[i - 1] ==  minimum_dif:
                answer.append([arr[i - 1], arr[i]])
        return answer