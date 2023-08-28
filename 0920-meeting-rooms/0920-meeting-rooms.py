def can_attend_meetings(intervals) -> bool:
    intervals.sort()
    lastEnd = intervals[0][1]
    
    for start, end in intervals[1:]:
        # Non overlap scenario
        if start >= lastEnd:
            lastEnd = end
        else:
            return False
    return True

print(can_attend_meetings([(5,8),(9,15)]))
