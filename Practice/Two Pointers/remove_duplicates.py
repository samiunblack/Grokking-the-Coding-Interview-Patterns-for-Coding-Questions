#Solution
# one pointer for non duplicate
# another for iterating

from os import remove


def remove_duplicates(arr):
    next_non_duplicate = 1
    next = 1
    
    while next < len(arr):
        if arr[next_non_duplicate - 1] != arr[next]:
            arr[next_non_duplicate] = arr[next]
            next_non_duplicate += 1
        next += 1
    
    return next_non_duplicate

def main():
    arr1 = [2, 3, 3, 3, 6, 9, 9]
    print("After removing duplicate element count: " + str(remove_duplicates(arr1)))
    
    arr2 = [2, 2, 2, 11]
    print("After removing duplicate element count: " + str(remove_duplicates(arr2)))
    
    
main()