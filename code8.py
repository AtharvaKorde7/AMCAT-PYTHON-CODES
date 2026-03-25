city = input("Enter the name of city: ")
scity = city.strip().lower()

if scity == 'hyderabad':
    print("Hello Hyderabad....Adab")
elif scity == 'mumbai':
    print("Hello Mumbai....Namaskar")
elif scity == 'delhi':
    print("Hello Delhi....Namaste")
elif scity == 'chennai':
    print("Hello Chennai....Vanakkam")
else:
    print("City is not in the list")