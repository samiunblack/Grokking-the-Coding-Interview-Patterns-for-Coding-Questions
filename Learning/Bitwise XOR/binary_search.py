def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return - 1

def main():
    print("Index of target is " + str(binary_search([1, 2, 3, 4, 5], 3)))
    print("Index of target is " + str(binary_search([23, 21, 45, 65, 75], 45)))
    print("Index of target is " + str(binary_search([23, 34, 45, 56, 76], 32)))
    
main()