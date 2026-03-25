n1 = int(input('Enter the value of paper1: '))
n2 = int(input('Enter the value of paper2: '))
n3 = int(input('Enter the value of paper3: '))

if n1 > n2:
    if n1 > n3:
        print("n1 is greater")
    else:
        print("n3 is greater")
else:
    if n2 > n3:
        print("n2 is greater")
    else:
        print("n3 is greater")

if n1 < n2:
    if n1 < n3:
        print("n1 is smaller")
    else:
        print("n3 is smaller")
else:
    if n2 < n3:
        print("n2 is smaller")
    else:
        print("n3 is smaller")