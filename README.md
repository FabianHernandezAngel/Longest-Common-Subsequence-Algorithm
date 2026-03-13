# Longest-Common-Subsequence-Algorithm
This project demonstrates a dynamic programming implementation of the Longest Common Subsequence problem. Given two strings and indices c1 and c2, the algorithm finds the length of the longest subsequence that appears in the first c1 characters of string a and the first c2 characters of string b.

# Example
Given string a = "skullandbones" and string b = "lullabybabies", the algorithm will print the length 7, as "ullabes" is the longest common substring of the pair.

# Algorithm
```
string_a = "skullandbones"
string_b = "lullabybabies"

# Initialize cache with dimensions (len(a)+1) x (len(b)+1)
cache = [[-1] * (len(string_b) + 1) for _ in range(len(string_a) + 1)]

def lcs(a, b, c1, c2):
    # Base case: empty string
    if c1 == 0 or c2 == 0:
        return 0
    
    # Return cached result if available
    if cache[c1][c2] != -1:
        return cache[c1][c2]
    
    # If characters match, add 1 to LCS of remaining strings
    if a[c1 - 1] == b[c2 - 1]:
        cache[c1][c2] = 1 + lcs(a, b, c1 - 1, c2 - 1)
    else:
        # If characters don't match, take max and ignore one character
        cache[c1][c2] = max(lcs(a, b, c1 - 1, c2), lcs(a, b, c1, c2 - 1))
    
    return cache[c1][c2]
```

# Time Complexity
* Each cell in the matrix (c1,c2) from 1..a and 1..b is computed once O(m*n)
* All other operations are O(n)
* Runtime is O(a * b), where a = len(a), b = len(b)
