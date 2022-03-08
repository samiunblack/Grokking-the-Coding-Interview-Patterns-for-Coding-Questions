def binaru_seach(arr, target):
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] < arr[end]
    
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == target:
            return mid
        
        else:
            if is_ascending:
                if arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if arr[mid] < target:
                    end = mid - 1
                else:
                    start = mid + 1
                    
def main():
    print(binaru_seach([4, 6, 10], 10))
    print(binaru_seach([1, 2, 3, 4, 5, 6, 7], 5))
    print(binaru_seach([10, 6, 4], 10))
    print(binaru_seach([10, 6, 4], 4))
    
main()