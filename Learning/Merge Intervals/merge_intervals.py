class Intervals:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end="")
        
    
    def __lt__(self, other):
        return self.end < other.end
        

def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    
    
    #sort the intervals on start time
    intervals.sort(key = lambda x: x.start)
    
    merged = []
    
    start = intervals[0].start
    end = intervals[0].end
    
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        
        if curr_interval.start <= end:
            end = max(end, curr_interval.end)
        
        else:
            merged.append(Intervals(start, end))
            start = intervals[i].start
            end = intervals[i].end  
    
    merged.append(Intervals(start, end))
    
    return merged

