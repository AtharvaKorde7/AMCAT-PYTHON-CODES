name = input("Enter a string: ")

vowels = 0
consonants = 0

for i in name:
    if i.lower() in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)