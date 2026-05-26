# Problem: Longest Substring Without Repeating Characters
# Platform: LeetCode
# Difficulty: Medium
# Approach: Sliding Window + Set
# Time Complexity: O(n)
# Space Complexity: O(n)

def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    maxLength = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxLength = max(maxLength, right - left + 1)
    return maxLength

s = "abcabcbb"
print(lengthOfLongestSubstring(s))