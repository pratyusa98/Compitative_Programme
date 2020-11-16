def sum_of_elements(arr, n):
    sumfirst = 0
    sumsecond = 0
    for i in range(n):
        if (i < n // 2):
            sumfirst += arr[i]
        else:
            sumsecond += arr[i]
    balance = sumfirst - sumsecond
    print(abs(balance))


# Driver Code
arr = [ 1, 2, 1, 2, 1, 3]

n = len(arr)


sum_of_elements(arr, n)
