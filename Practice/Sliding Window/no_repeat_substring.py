#Solution
# keep the non repeating characters in a hashmap
#if character is in the hashmap then keep removing elements from the beginning
#until all is non repeating in the hashmap

def no_repeat_substring(str):
    window_start = 0
    longest_substring = 0
    
    char_frequency = {}
    
    for window_end in range(len(str)):
        current_char = str[window_end]
        
        if current_char in char_frequency:
            window_start = max(window_start, char_frequency[current_char] + 1)
        
        char_frequency[current_char] = window_end
    
        longest_substring = max(longest_substring, window_end - window_start + 1)
        
    return longest_substring


def main():
    str1 = "aabccbb"
    print("Longest substring without repeat: " + str(no_repeat_substring(str1)))
    
    str2 = "abbbb"
    print("Longest substring without repeat: " + str(no_repeat_substring(str2)))
    
    str3 = "abccde"
    print("Longest substring without repeat " + str(no_repeat_substring(str3)))
    
main()