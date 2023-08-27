class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(intervals)):
            # Comes before the interval
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]

            # Comes after the interval
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])

            # Overlaps with the interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        output.append(newInterval)
        return output
