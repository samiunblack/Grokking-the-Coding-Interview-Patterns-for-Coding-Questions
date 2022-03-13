def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square(slow)
        fast = find_square(find_square(fast))

        if slow == fast:
            break
    
    return slow == 1

def find_square(num):
    sum = 0
    
    while(num > 0):
        digit = num % 10
        sum += digit * digit
        num //= 10
    
    return sum

def main():
    print("Happy Number " + str(find_happy_number(23)))
    print("Happy Number " + str(find_happy_number(12)))
    
main()