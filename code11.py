per = int(input('Enter your percentage: '))

if per >= 90:
    print("A")
elif per >= 80 and per < 90:
    print("B")
elif per >= 60 and per < 80:
    print("C")
else:
    print("FAIL")