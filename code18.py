arr = [10, 20, 30, 40, 50, 60]
target = int(input("Enter element to search: "))

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
        print("Element found at index:", mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")