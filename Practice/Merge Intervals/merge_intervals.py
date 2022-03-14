class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def print_intervals(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')
    

def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals;
    
    intervals.sort(key=lambda x: x.start)
    
    start = intervals[0].start
    end = intervals[0].end
    
    merged_intervals = []
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end
            
    merged_intervals.append(Interval(start, end))
    
    return merged_intervals


def main():
    print("Merged Intervals: ", end='')
    for i in merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_intervals()
    print()

    print("Merged Intervals: ", end='')
    for i in merge_intervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_intervals()
    print()
    
main()