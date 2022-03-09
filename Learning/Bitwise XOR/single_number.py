def single_number(nums):
    num = 0
    
    for i in nums:
        num ^= i
    
    return num

def main():
    print("Single number: " + str(single_number([1, 4, 2, 1, 3, 2, 3])))
    print("Single number: " + str(single_number([7, 9, 7])))
    
main()