class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e:e[0])
        output = []
        i = 0
        while i < len(intervals) - 1:
            start = min(intervals[i][0], intervals[i+1][0])
            end = max(intervals[i+1][1], intervals[i][1])
            if intervals[i][1] >= intervals[i+1][0]:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [start, end])
                continue
            i += 1

        return intervals