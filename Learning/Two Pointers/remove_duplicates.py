def remove_duplicates(arr):
    #my way
    first_ptr = 0
    second_ptr = 1

    while second_ptr < len(arr):
        if arr[first_ptr] == arr[second_ptr]:
            arr.pop(second_ptr)

        elif arr[second_ptr] > arr[first_ptr]:
            first_ptr = second_ptr
            second_ptr = second_ptr + 1

    return len(arr)

def remove_duplicates(arr):
    #easier way
    
    next_non_duplicate = 1
    
    i = 1
    
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    
    return next_non_duplicate
        
        

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))
