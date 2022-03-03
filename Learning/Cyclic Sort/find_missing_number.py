def find_missing_number(nums):
    start = 0

    while start < len(nums):
        correct_pos = nums[start]

        if nums[start] < len(nums) and nums[start] != nums[correct_pos]:
            nums[start], nums[correct_pos] = nums[correct_pos], nums[start]

        else:
            start += 1
    
    for i in range(len(nums)):
        if nums[i] != i:
            return i


print(find_missing_number([4, 0, 3, 1]))
