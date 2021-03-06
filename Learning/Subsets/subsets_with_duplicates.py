def subsets_with_duplicates(nums):
    nums.sort()
    
    subsets = []
    subsets.append([])
    
    start_index, end_index = 0, 0
    
    for i in range(len(nums)):
        start_index = 0
        
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        
        for j in range(start_index, end_index + 1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    
    return subsets



print("List of subsets: " + str(subsets_with_duplicates([1, 3, 3])))
