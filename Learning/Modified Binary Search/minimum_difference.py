def minimum_difference(arr, key):
    
    start, end = 0 , len(arr) - 1
    
    if key < arr[start]:
        return arr[start]
    if key > arr[end]:
        return arr[end]
    
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]

def main():
    print(minimum_difference([4, 6, 10], 7))
    print(minimum_difference([4, 6, 10], 4))
    print(minimum_difference([1, 3, 8, 10, 15], 12))
    print(minimum_difference([4, 6, 10], 17))
    
main()