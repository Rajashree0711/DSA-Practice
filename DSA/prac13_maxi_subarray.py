# Problem: Maximum Subarray
# Platform: LeetCode
# Difficulty: Medium
# Approach: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSubArray(nums):
    current = nums[0]
    best = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(best, current)
    return best

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))