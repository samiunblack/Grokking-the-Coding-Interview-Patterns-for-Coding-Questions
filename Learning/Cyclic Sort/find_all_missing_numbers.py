def find_all_missing_nums(nums):
    length = len(nums)
    start = 0
    
    while start < length:
        correct_pos = nums[start] - 1
        
        if nums[start] != nums[correct_pos]:
            nums[start], nums[correct_pos] = nums[correct_pos], nums[start]
        
        else:
            start += 1
    
    missing_nums = []
    
    for i in range(length):
        if nums[i] != i + 1:
            missing_nums.append(i + 1)
        
    return missing_nums


print(find_all_missing_nums([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_all_missing_nums([2, 4, 1, 2]))
print(find_all_missing_nums([2, 3, 2, 1]))