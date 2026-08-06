class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        answer = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        overlap = False
        last_num = None
        for i in range(n):
            if i == 0:
                index = i
                cur_end = intervals[0][1]
                continue
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= cur_end:
                if last_num is not None and i == last_num + 1:
                    answer.pop()
                cur_end = max(end, cur_end)
                overlap = True
                continue
            if i == 1 and overlap == False:
                answer.append(intervals[0])
            if overlap == True:
                answer.append([intervals[index][0], cur_end])
                overlap = False
            answer.append([start, end])
            last_num = i
            cur_end = end
            index = i
        if answer == [] and intervals != [[]]:
            answer.append([intervals[index][0], cur_end])
        elif overlap:
            answer.append([intervals[index][0], cur_end])
        return answer