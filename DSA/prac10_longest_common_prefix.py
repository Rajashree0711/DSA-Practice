# Problem: Longest Common Prefix
# Platform: LeetCode
# Difficulty: Easy
# Approach: Prefix Shrinking
# Time Complexity: O(n * m)
# Space Complexity: O(1)

def longestCommonPrefix(strs):
    prefix = strs[0]
    for word in strs[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
    return prefix

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))