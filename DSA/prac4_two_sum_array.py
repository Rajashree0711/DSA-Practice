# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy
# Approach: Hash Map (Dictionary)
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))