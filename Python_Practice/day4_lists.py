# SORT VS SORTED
nums = [4, 1, 3, 2]
nums.sort()
print(nums)
nums2 = [7, 5, 9, 1]
new_list = sorted(nums2)
print(new_list)
print(nums2)
print("-------------")

# LIST COMPREHENSION
squares = [x * x for x in range(5)]
print(squares)
print("-------------")

# EVEN NUMBERS
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
print("-------------")

# STUDENT MARKS
marks = [78, 90, 67, 88, 95, 72, 60, 81, 85, 77]
total = 0
maximum = marks[0]
minimum = marks[0]
for mark in marks:
    total += mark
    if mark > maximum:
        maximum = mark
    if mark < minimum:
        minimum = mark
average = total / len(marks)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("-------------")

# PASS / FAIL
marks2 = [45, 67, 32, 89, 90, 20]
passed = [m for m in marks2 if m >= 50]
failed = [m for m in marks2 if m < 50]
print("Passed:", passed)
print("Failed:", failed)
print("-------------")

# COUNT ABOVE
def count_above(lst, threshold):
    count = 0
    for num in lst:
        if num > threshold:
            count += 1
    return count

nums3 = [10, 20, 30, 40, 50]
print(count_above(nums3, 25))