from merge_intervals import Intervals
from heapq import *

def min_meeting_rooms(meetings):
    room_required = 0
    
    meetings.sort(key= lambda x: x.start)
    
    minheap = []
    
    for meeting in meetings:
        
        while len(minheap) > 0 and meeting.start >= minheap[0].end:
            heappop(minheap)
            
        heappush(minheap, meeting)
            
        room_required = max(room_required, len(minheap))
            
    return room_required


meetings = [Intervals(4, 5), Intervals(2, 3), Intervals(2, 4), Intervals(3, 5)]

print(min_meeting_rooms(meetings))