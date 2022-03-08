def subsets(nums):
    subsets = []
    
    subsets.append([])
    
    for current_num in nums:
        n = len(subsets)
        
        for i in range(n):
            set = list(subsets[i])
            set.append(current_num)
            subsets.append(set)
    
    return subsets

print("List of subset: " + str(subsets([1, 5, 3])))            