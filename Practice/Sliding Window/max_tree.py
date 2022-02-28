def minimumTime(time, totalTrips) -> int:
        result = 0
        
        time.sort()
        i = time[0]
        while result < totalTrips:    
            for t in time:
                if t <= i and t % i == 0:
                    result += 1
            
            i+= 1
        
        return i - 1


print(minimumTime([1,2,3], 5))
