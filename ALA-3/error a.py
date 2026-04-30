arr = [29, 10, 14, 37, 13]
n = len(arr)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

# print result
for x in arr:
    print(x, end=" ")