# Problem: Remove Duplicates from Sorted Array
# Platform: LeetCode
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def removeDuplicates(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1

nums = [1,1,2,2,3,4,4]
k = removeDuplicates(nums)
print("Unique Count:", k)
print("Modified Array:", nums[:k])