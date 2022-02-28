def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highest_ptr = n - 1
    left, right = 0, n - 1
    
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        
        if left_square > right_square:
            squares[highest_ptr] = left_square
            left += 1
        else:
            squares[highest_ptr] = right_square
            right -= 1
        
        highest_ptr -= 1
    
    return squares
        
print(make_squares([-3, -1, 0, 1, 2]))