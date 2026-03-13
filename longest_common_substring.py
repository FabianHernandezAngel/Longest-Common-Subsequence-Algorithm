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


if __name__ == "__main__":
    print(lcs(string_a, string_b, len(string_a), len(string_b)))