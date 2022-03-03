def find_first_k_missing_positive(nums, K):
    length = len(nums)
    start = 0
    
    while start < length:
        correct_pos = nums[start] - 1
        
        if nums[start] > 0 and nums[start] <= len(nums) \
            and nums[start] != nums[correct_pos]:
            nums[start], nums[correct_pos] = nums[correct_pos], nums[start]
        else:
            start += 1
    
    result = []
    extra_nums = set()
    for i in range(length):
        if nums[i] != i + 1:
            if len(result) < K:
                result.append(i + 1)
                extra_nums.add(nums[i])
    
    i = 1
    while len(result) < K:
        candidate = length + i
        if candidate not in extra_nums:
            result.append(candidate) 
        i += 1       
    
    return result


print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
print(find_first_k_missing_positive([2, 3, 4], 3))
print(find_first_k_missing_positive([-2, -3, 4], 2))