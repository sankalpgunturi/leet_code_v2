def min_meeting_rooms(intervals) -> int:
    # Intuitive Code
    # start, end = [], []
    
    # for s, e in intervals:
    #     start.append(s)
    #     end.append(e)
    
    # start.sort()
    # end.sort()
    
    # Concize code
    st, en = zip(*intervals)
    print(st, en)
    start = sorted(st)
    end = sorted(en)

    s, e, count, maxCount = 0, 0, 0, 0
    while s < len(start):
        if min(start[s], end[e]) == start[s]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        
        maxCount = max(count, maxCount)
            
    return maxCount
    
print(min_meeting_rooms([(0,30),(5,10),(15,20)]))
# print(min_meeting_rooms([(2,7)]))
