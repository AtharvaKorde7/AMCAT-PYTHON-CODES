nums = [2, 7, 11, 15]
target = int(input("Enter target: "))

hashmap = {}

for i, num in enumerate(nums):
    diff = target - num
    
    if diff in hashmap:
        print("Indices:", hashmap[diff], i)
        break
    
    hashmap[num] = i
else:
    print("No solution found")