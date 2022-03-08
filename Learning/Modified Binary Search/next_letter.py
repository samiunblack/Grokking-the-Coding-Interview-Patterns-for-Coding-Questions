def next_letter(arr, key):
    n = len(arr)
    
    if key < arr[0] or key > arr[n - 1]:
        return arr[0]
    
    start, end = 0, n - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return arr[start % n]
    
def main():
    print(next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
        