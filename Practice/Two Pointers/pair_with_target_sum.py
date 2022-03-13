#Solution
# Just throw a hashmap :)

def find_pair_sum(arr, target):
    nums = {}
    
    for i in range(len(arr)):
        current_num = arr[i]
        pair = target - current_num
        
        if pair not in nums:
            nums[current_num] = i
        else:
            return [nums[pair], i]

def main():
    arr1 = [1, 2, 3, 4, 6]
    print("Pair Sum: " + str(find_pair_sum(arr1, 6)))
    
    arr2 = [2, 5, 9, 11]
    print("Pair Sum: " + str(find_pair_sum(arr2, 11)))

main()