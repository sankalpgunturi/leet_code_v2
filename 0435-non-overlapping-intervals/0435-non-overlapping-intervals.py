class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0

        # Collecting the end element of the first pair
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # Is the start element of the current interval > than the lastEnd end elem
            # Not considered as overlap
            if start >= lastEnd:
                lastEnd = end
            else:
                # There is an overlap
                count += 1
                lastEnd = min(lastEnd, end)
        return count
