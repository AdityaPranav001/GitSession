# Define an array (list in Python)
arr = [10, 20, 30, 40, 50]
size = 5
index = 2

# Shift elements left to overwrite the target index
for i in range(index, size - 1):
    arr[i] = arr[i + 1]

# Reduce the size to remove the last duplicate element
size -= 1

# Print the updated array
print("Array after deletion:", end=" ")
for i in range(size):
    print(arr[i], end=" ")
print()