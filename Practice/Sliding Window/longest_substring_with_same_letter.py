#Solution
# make a hashmap with all the elements of string
# get the character that appears the most
# if adding K to the characters appearing number doesn't fit the window then
# shrink the window

def longest_substring(str, K):
    char_frequency = {}
    
    for char in str:
        if char not in char_frequency:
            char_frequency[char] = 0
        
        char_frequency[char] += 1
    
    max_key = max(char_frequency, key=char_frequency.get)
    
    return char_frequency[max_key] + K
    
        

def main():
    print("Longest Substring: " + str(longest_substring("aabccbb", 2)))
    print("Longest Substring: " + str(longest_substring("abbcb", 1)))
    print("Longest Substring: " + str(longest_substring("abccde", 1)))
    
main()