n = int(input("Enter the size of the array: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter value for element {i + 1}: ")))

arr.sort
max_val = arr[0]
second_max = -1

for i in range(1, n):
    if arr[i] > max_val:
        second_max = max_val
        max_val = arr[i]
    elif arr[i] > second_max and arr[i] != max_val:
        second_max = arr[i]

if second_max == -1:
    print("No second largest element found, all elements are the same")
else:
    print(f"The second largest value is: {second_max}")
