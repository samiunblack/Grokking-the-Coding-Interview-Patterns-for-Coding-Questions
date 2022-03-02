from merge_intervals import Intervals

def insert_intervals(intervals, new_interval):      
    merged = []
    
    start = intervals[0].start
    end = intervals[0].end
    
    j = 0
    while new_interval not in intervals:
        interval = intervals[j]
        if interval.end <= new_interval.start:
            intervals.insert(j + 1, new_interval)
        j += 1
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        
        
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Intervals(start, end))
            start = interval.start
            end = interval.end
    
    merged.append(Intervals(start, end))
    
    return merged

def insert_intervals(intervals, new_interval):
    merged = []
    
    i = 0
    
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1
    
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(new_interval.start, intervals[i].start)
        new_interval.end = max(new_interval.end, intervals[i].end)
        i+= 1
    
    merged.append(new_interval)
    
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged
    

intervals = [Intervals(1, 3), Intervals(5, 7), Intervals(8, 12)]

for i in insert_intervals(intervals, Intervals(4, 6)):
    i.print_interval()
print()