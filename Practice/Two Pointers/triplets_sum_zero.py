#Solution

# X + Y + Z = 0; Y + Z = -X
# skip same element fro unique triplet

def search_triplet(arr):
    arr.sort()
    triplets = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        find_triplets(arr, -arr[i], i + 1, triplets)
    
    return triplets

def find_triplets(arr, target, left, triplets):
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
        
        while left < right and arr[left] == arr[left - 1]:
            left += 1
        