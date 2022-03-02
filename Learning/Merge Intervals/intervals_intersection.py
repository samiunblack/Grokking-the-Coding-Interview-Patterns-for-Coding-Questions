from merge_intervals import Intervals

def intervals_intersection(arr1, arr2):
    i, j = 0, 0
    
    result = []
    
    while i < len(arr1) and j < len(arr2):
        a = arr1[i]
        b = arr2[j]
        
        a_overlaps_b = a.start >= b.start and a.start <= b.end
        b_overlaps_a = b.start >= a.start and b.start <= a.end
        
        if a_overlaps_b or b_overlaps_a:
            start = max(a.start, b.start)
            end = min(a.end, b.end)
            result.append(Intervals(start, end))
        
        if a.end < b.end:
            i += 1
        else:
            j += 1
        
        
    return result

intervals1 = [Intervals(1, 3), Intervals(5, 6), Intervals(7, 9)]
intervals2 = [Intervals(2, 3), Intervals(5, 7)]

for i in intervals_intersection(intervals1, intervals2):
    i.print_interval()
print()