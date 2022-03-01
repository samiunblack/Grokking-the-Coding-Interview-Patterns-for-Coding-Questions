def happy_number(num):
    slow, fast = num, num
    
    while True:
        slow = find_square(slow) #moves one step
        fast = find_square(find_square(fast)) #moves two steps
        
        if slow == fast:
            break
    
    return slow == 1

def find_square(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    
    return _sum

print(happy_number(12))