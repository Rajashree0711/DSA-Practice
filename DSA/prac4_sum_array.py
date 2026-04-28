# Problem: Running Sum of 1D Array
# Platform: LeetCode
# Difficulty: Easy
# Approach: Cumulative Sum (Prefix Sum)
# Time Complexity: O(n)
# Space Complexity: O(n)
def runningSum(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result
nums = [1,2,3,4]    
print(runningSum(nums))