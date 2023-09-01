class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        output = []
        flag = False
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0] and flag == False:
                output.append(newInterval)
                flag = True
            output.append(interval)
        if len(output) == len(intervals):
            output.append(newInterval)

        i = 0
        while i < len(output) - 1:
            currEnd, nextStart = output[i][1], output[i + 1][0]
            currStart, nextEnd = output[i][0], output[i + 1][1]
            if currEnd >= nextStart:
                output.pop(i)
                output.pop(i)
                output.insert(i, [min(currStart, nextStart), max(currEnd, nextEnd)])
                i = 0
                continue
            i += 1

        return output
