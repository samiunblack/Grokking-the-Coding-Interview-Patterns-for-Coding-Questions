#Solution
# keep a hashmap of characters. If length of hashmap is greater than 2 shrink
# the window from beginning

def fruits_into_baskets(fruits):
    window_start, max_fruit = 0, 0
    
    basket = {}
    
    for window_end in range(len(fruits)):
        fruit = fruits[window_end]  
        if fruit not in basket:
            basket[fruit] = 0
        basket[fruit] += 1
        
        while len(basket) > 2:
            first_fruit = fruits[window_start]
            basket[first_fruit] -= 1
            if basket[first_fruit] == 0:
                del basket[first_fruit]
            
            window_start += 1
        
        max_fruit = max(max_fruit, window_end - window_start + 1)
    
    return max_fruit

    
def main():
    fruits1 = ['A', 'B', 'C', 'A', 'C']
    print("max fruits into basket: %s" % str(fruits_into_baskets(fruits1)))
    
    fruits2 = ['A', 'B', 'C', 'B', 'B', 'C']
    print("max fruits into basket: %s" % str(fruits_into_baskets(fruits2)))

main()