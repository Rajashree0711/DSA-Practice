# Problem: Valid Palindrome
# Platform: LeetCode
# Difficulty: Easy
# Approach: Two Pointers + String Cleaning
# Time Complexity: O(n)
# Space Complexity: O(n)

def isPalindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))