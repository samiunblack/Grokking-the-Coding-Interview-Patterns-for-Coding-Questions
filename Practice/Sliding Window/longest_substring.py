#Solution
#add the elements in a hashmap until the map contains more than K elements
#when the map contains more than K elements remove a element from the beginning
#update the longest substring on every iteration

def longest_substring(str, K):
    window_start, longest = 0, 0
    
    char_frequency = {}
    
    for window_end in range(len(str)):
        current_char = str[window_end]
        
        if current_char not in char_frequency:
            char_frequency[current_char] = 0
        
        char_frequency[current_char] += 1
        
        while len(char_frequency) > K:
            start_char = str[window_start]
            char_frequency[start_char] -= 1
            if char_frequency[start_char] == 0:
                del char_frequency[start_char]
            
            window_start += 1
        
        longest = max(longest, window_end - window_start + 1)
    
    return longest


def main():
    str1 = "araaci"
    print("longest substring: %s" % str(longest_substring(str1, 2)))
    
    str2 = "araaci"
    print("longest substring: %s" % str(longest_substring(str2, 1)))
    
    str3 = "cbbebi"
    print("longest substring: %s" % str(longest_substring(str3, 3)))
    
main()