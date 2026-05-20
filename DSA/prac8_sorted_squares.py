# Problem: Squares of a Sorted Array
# Platform: LeetCode
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    position = len(nums) - 1
    result = [0] * len(nums)
    while left <= right:
        lefts = nums[left] * nums[left]
        rights = nums[right] * nums[right]
        if lefts > rights:
            result[position] = lefts
            left += 1
        else:
            result[position] = rights
            right -= 1
        position -= 1
    return result

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))