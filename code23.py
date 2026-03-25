expr = input("Enter expression: ")

stack = []
pairs = {')': '(', '}': '{', ']': '['}

for char in expr:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if not stack or stack[-1] != pairs[char]:
            print("Not Balanced")
            break
        stack.pop()
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")