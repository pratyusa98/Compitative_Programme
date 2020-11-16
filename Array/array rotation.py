
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range( n -1):
        arr[i] = arr[ i +1]
    arr[ n -1] = temp

def beforArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")

def printArray(arr,size):
    for i in range(size):
        print ("%d"% arr[i],end=" ")





arr =[12, 10, 5, 6, 52, 36]

beforArray(arr,len(arr))
leftRotate(arr,2,len(arr))
print("")
printArray(arr, len(arr))
