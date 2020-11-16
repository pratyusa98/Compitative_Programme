def minNum(arr, n):
    # Count odd number of terms in array
    odd = 0
    for i in range(n):
        if (arr[i] % 2):
            odd += 1

    if (odd % 2):
        return 1
    return 2


# Driver code 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print (minNum(arr, n))