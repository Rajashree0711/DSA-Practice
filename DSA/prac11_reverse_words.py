# Problem: Reverse Words in a String
# Platform: LeetCode
# Difficulty: Medium
# Approach: Split + Reverse + Join
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverseWords(s):
    words = s.split()
    reverse = words[::-1]
    answer = ' '.join(reverse)
    return answer

s = "the sky is blue"
print(reverseWords(s))