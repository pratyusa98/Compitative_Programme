

def kthsmallest(arr,k):
    arr.sort()
    return arr[k-1]


t = int(input())

for i in range(t):
    arr = []
    n = int(input("Enter number of elements : "))
    for j in range(0, n):
        ele = int(input())
        arr.append(ele)
    k = int(input())
    print(kthsmallest(arr,k))



