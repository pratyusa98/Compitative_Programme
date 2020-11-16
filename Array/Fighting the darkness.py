
def maxDays(arr,n):
    maxx = -1
    x = 0
    for i in range(0,n):
        x = arr[i]
        if (x > maxx):
            maxx = x;
    return maxx



arr = [1,1,2]
n = 3
print(maxDays(arr,n))