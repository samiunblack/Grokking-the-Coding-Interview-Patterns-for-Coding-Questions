#Solution
# two pointers at two ends
# biggest result in the result array


def make_squares(arr):
    left_ptr = 0
    right_ptr = len(arr) - 1
    highest_index = len(arr) - 1
    result = [0] * len(arr)
    
    while left_ptr <= right_ptr:
        left_square = arr[left_ptr] * arr[left_ptr]
        right_square = arr[right_ptr] * arr[right_ptr]
        
        if left_square > right_square:
            result[highest_index] = left_square
            left_ptr += 1
        else:
            result[highest_index] = right_square
            right_ptr -= 1
        highest_index -= 1
    
    return result

def main():
    arr1 = [-2, -1, 0, 2, 3]
    print(make_squares(arr1))
    
    arr2 = [-3, -1, 0, 1, 2]
    print(make_squares(arr2))
    
main()