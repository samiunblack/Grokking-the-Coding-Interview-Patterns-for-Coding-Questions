def number_range(arr, key):
    result = [-1, -1]
    
    result[0] = binary_search(arr, key, False)
    
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)
    
    return result
    
    
def binary_search(arr, key, findMax):
    start, end = 0, len(arr) - 1
    keyIndex = -1
    
    while start <= end:
        mid = (start + end)//2
        
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            keyIndex = mid
            
            if findMax:
                start = mid + 1 #search ahead to find the last index of 'key'
            else:
                end = mid - 1 # search behind to find the first index of 'key'
    
    return keyIndex

def main():
    print(number_range([4, 6, 6, 6, 9], 6))
    print(number_range([1, 3, 8, 10, 15], 10))
    print(number_range([1, 3, 8, 10, 15], 12))
    
main()
        