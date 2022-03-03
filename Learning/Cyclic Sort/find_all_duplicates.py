def find_all_duplicates(nums):
    length = len(nums)
    start = 0
    
    while start < length:
        correct_pos = nums[start] - 1
        
        if nums[start] != nums[correct_pos]:
            nums[start], nums[correct_pos] = nums[correct_pos], nums[start]
        else:
            start += 1

    duplicate_nums = []
    
    for i in range(length):
        if nums[i] != i + 1:
            duplicate_nums.append(nums[i])
    
    return duplicate_nums

print(find_all_duplicates([3, 4, 4, 5, 5]))
print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))