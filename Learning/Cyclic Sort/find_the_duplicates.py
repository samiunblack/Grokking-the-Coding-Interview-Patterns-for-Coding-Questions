def find_duplicates(nums):
    length = len(nums)
    start = 0
    
    while start < length:
        if nums[start] != start + 1:
            correct_pos = nums[start] - 1
        
            if nums[start] != nums[correct_pos]:
                nums[start], nums[correct_pos] = nums[correct_pos], nums[start]
            
            else:
                return nums[start]
        else:
            start += 1
    
    return -1


print(find_duplicates([1, 4, 4, 3, 2]))
print(find_duplicates([2, 1, 3, 3, 5, 4]))
print(find_duplicates([2, 4, 1, 4, 4]))