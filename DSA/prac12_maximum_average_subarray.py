# Problem: Maximum Average Subarray I
# Platform: LeetCode
# Difficulty: Easy
# Approach: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

def findMaxAverage(nums, k):
    windowSum = sum(nums[:k])
    maxSum = windowSum
    for right in range(k, len(nums)):
        windowSum = windowSum - nums[right - k]
        windowSum = windowSum + nums[right]
        maxSum = max(maxSum, windowSum)
    return maxSum / float(k)

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))