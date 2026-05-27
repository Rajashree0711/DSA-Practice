import json

# DICTIONARY
student = {
    "name": "Selin",
    "marks": 95
}
print(student.get("name"))
print(student.get("city", "Not Found"))
print("-------------")

# WORD FREQUENCY COUNTER
text = "apple banana apple mango banana apple"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
print("-------------")

# FILE WRITE
with open("demo.txt", "w") as file:
    file.write("Hello World")

# FILE READ
with open("demo.txt", "r") as file:
    content = file.read()
print(content)
print("-------------")

# JSON SAVE
data = {
    "name": "Selin",
    "age": 20
}
with open("data.json", "w") as file:
    json.dump(data, file)

# JSON LOAD
with open("data.json", "r") as file:
    loaded = json.load(file)
print(loaded)
print("-------------")

# CONTACT BOOK
contacts = {}
def add_contact(name, number):
    contacts[name] = number
def search_contact(name):
    return contacts.get(name, "Not Found")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
add_contact("Selin", "9876543210")
print(search_contact("Selin"))
delete_contact("Selin")
print(contacts)
print("-------------")

# TWO SUM
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
print(two_sum([2, 7, 11, 15], 9))