import math

class ArrayReader:
    
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

def binary_search(reader, key):
    size = 2
    start, end = 0, size - 1
    
    
    while start <= end:
        mid = (start + end)//2
        
        midValue = reader.get(mid)
        if midValue == key:
            return mid
        
        if midValue < key:
            start = mid + 1
            size = size * 2
            end = size - 1
        
        if midValue > key:
            end = mid - 1
    
    return -1

def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(binary_search(reader, 16))
    print(binary_search(reader, 11))
    
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(binary_search(reader, 15))
    print(binary_search(reader, 200))
    
main()
