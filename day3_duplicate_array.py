# Problem: Contains Duplicate
# Platform: LeetCode
# Difficulty: Easy
# Approach: Set
# Time: O(n)
# Space: O(n)
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
nums = [1,2,3,1]
print(containsDuplicate(nums))