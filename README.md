# Grokking-the-Coding-Interview-Patterns-for-Coding-Questions

## Pattern 1: Sliding Window

### Notes: 
![Screenshot from 2022-02-26 05-41-05.png](https://hackernoon.com/_next/image?url=https%3A%2F%2Fcdn.hackernoon.com%2Fimages%2FG9YRlqC9joZNTWsi1ul7tRkO6tv1-8i6d3wi0.jpg&w=2048&q=75)

The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks.

**Following are some ways you can identify that the given problem might require a sliding window**:

- The problem input is a linear data structure such as a linked list, array, or string
- You’re asked to find the longest/shortest substring, subarray, or a desired value

**Common problems you use the sliding window pattern with**:

- Maximum sum subarray of size ‘K’ (easy)
- Longest substring with ‘K’ distinct characters (medium)
- String anagrams (hard)


## Problems:
- [Maximum sum subarray of size K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)
- [Smallest subarray with given sum](https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/)
- [Longest substring with K distinct values](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/)
- [Fruit into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
- [No repeat substring](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Longest substring with same letter after replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [Longest substring with ones after replacement](https://www.geeksforgeeks.org/longest-subsegment-1s-formed-changing-k-0s/)

## Practice:
