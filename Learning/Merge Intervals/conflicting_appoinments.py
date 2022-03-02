from merge_intervals import Intervals

def conflicting_appointments(intervals):
    intervals.sort(key= lambda x: x.start)
    
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        prev_interval = intervals[i - 1]
        
        if interval.start < prev_interval.end:
            return False
    
    return True

intervals = [Intervals(4, 5), Intervals(2, 3), Intervals(3, 6)]

print(conflicting_appointments(intervals))