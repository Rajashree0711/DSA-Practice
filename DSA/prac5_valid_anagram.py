# Problem: Valid Anagram
# Platform: LeetCode
# Difficulty: Easy
# Approach: Hash Map (Dictionary Counting)
# Time Complexity: O(n)
# Space Complexity: O(n)

def isAnagram(s, t):
    countS = {}
    countT = {}
    for ch in s:
        countS[ch] = countS.get(ch, 0) + 1
    for ch in t:
        countT[ch] = countT.get(ch, 0) + 1
    return countS == countT

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))