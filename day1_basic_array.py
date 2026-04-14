arr = [15, 3, 99, 42, 7]
max_val = arr[0]
for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
print(max_val) 