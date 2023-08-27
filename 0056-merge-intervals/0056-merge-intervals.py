class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the list based on their start values
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        
        # Merge intervals
        for start, end in intervals[1:]:
            # print(start, end)
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
