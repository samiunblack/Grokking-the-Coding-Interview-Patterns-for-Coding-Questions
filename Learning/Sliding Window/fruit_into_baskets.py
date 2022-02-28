def fruit_into_baskets(fruit):
    fruit_basket = {}

    window_start = 0
    max_fruits = 0

    for window_end in range(len(fruit)):
        right_fruit = fruit[window_end]
        if right_fruit not in fruit_basket:
            fruit_basket[right_fruit] = 0
        
        fruit_basket[right_fruit] += 1

        while len(fruit_basket) > 2:
            left_fruit = fruit[window_start]
            fruit_basket[left_fruit] -= 1
            if fruit_basket[left_fruit] <= 0:
                del fruit_basket[left_fruit]    
            
            window_start += 1
        
        max_fruits = max(max_fruits, window_end - window_start + 1)
    
    return max_fruits


print(fruit_into_baskets(['A', 'B', 'C', 'A', 'C']))
print(fruit_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))