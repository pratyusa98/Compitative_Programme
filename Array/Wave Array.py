
def sortInWave(arr,x):
    # sort the array Step 1
    arr.sort()

    # Swap adjacent elements Step 2
    for i in range(0, x - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]



arr = [2,4,7,8,9,10]
sortInWave(arr, len(arr))
for i in range(0,len(arr)):
    print (arr[i],end=" ")