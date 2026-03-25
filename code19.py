s = input("Enter a string: ")

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequency:")
for k, v in freq.items():
    print(k, ":", v)        