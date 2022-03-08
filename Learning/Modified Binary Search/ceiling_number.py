def ceiling_of_number(arr, key):
    start, end = 0, len(arr) - 1
    
    if key > arr[end]:
        return -1
    
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

def main():
    print(ceiling_of_number([4, 6, 10], 6))
    print(ceiling_of_number([1, 3, 8, 10, 15], 12))
    print(ceiling_of_number([4, 6, 10], 17))
    print(ceiling_of_number([4, 6, 10], -1))

main()