def find_corrupt_pair(nums):
    length = len(nums)
    start = 0
    
    while start < length:
        correct_pos = nums[start] - 1
        
        if nums[start] != nums[correct_pos]:
            nums[start], nums[correct_pos] = nums[correct_pos], nums[start]
        
        else:
            start += 1
    
    for i in range(length):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
        
print(find_corrupt_pair([3, 1, 2, 5, 2]))
print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))