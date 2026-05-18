# Problem: Convert the Temperature
# Platform: LeetCode
# Difficulty: Easy
# Approach: Mathematical Formula
# Time Complexity: O(1)
# Space Complexity: O(1)

def convertTemperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
celsius = 36.50
print(convertTemperature(celsius))