from heapq import *

class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load
    
    def __lt__(self, other):
        return self.end < other.end

def find_max_cpu_load(jobs):
    
    jobs.sort(key=lambda x: x.start)
    
    max_cpu_load = 0
    current_cpu_load = 0
    
    min_heap = []
    
    for job in jobs:
        
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)
        
        heappush(min_heap, job)  
        current_cpu_load += job.cpu_load
        max_cpu_load = max(current_cpu_load, max_cpu_load)
    return max_cpu_load

print(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)]))