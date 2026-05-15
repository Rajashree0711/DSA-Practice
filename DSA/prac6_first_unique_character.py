# Problem: First Unique Character in a String
# Platform: LeetCode
# Difficulty: Easy
# Approach: Hash Map (Frequency Counting)
# Time Complexity: O(n)
# Space Complexity: O(n)

def firstUniqChar(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

s = "leetcode"
print(firstUniqChar(s))