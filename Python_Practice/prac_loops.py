# FOR LOOP
for i in range(5):
    print(i)

print("-------------")

# WHILE LOOP
count = 1

while count <= 5:
    print(count)
    count += 1

print("-------------")

# ENUMERATE
fruits = ["apple", "banana", "grape"]

for index, value in enumerate(fruits):
    print(index, value)

print("-------------")

# BREAK
for i in range(10):

    if i == 5:
        break

    print(i)

print("-------------")

# CONTINUE
for i in range(5):

    if i == 2:
        continue

    print(i)

print("-------------")

# MULTIPLICATION TABLE
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("-------------")

# SUM OF DIGITS
num = 1234
total = 0

while num > 0:

    digit = num % 10
    total += digit

    num = num // 10

print("Sum:", total)

print("-------------")

# FIBONACCI
n = 10

a = 0
b = 1

for i in range(n):

    print(a)

    temp = a + b
    a = b
    b = temp

print("-------------")

# PRIME NUMBERS
for num in range(2, 51):

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)