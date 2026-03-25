v1 = float(input("Enter value 1: "))
v2 = float(input("Enter value 2: "))
v3 = float(input("Enter value 3: "))
v4 = float(input("Enter value 4: "))
v5 = float(input("Enter value 5: "))

max_val = v1

if v2 > max_val:
    max_val = v2
if v3 > max_val:
    max_val = v3
if v4 > max_val:
    max_val = v4
if v5 > max_val:
    max_val = v5

print("Maximum value is:", max_val)