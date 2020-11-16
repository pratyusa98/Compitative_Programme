
def kthsmallest(arr,k):
    arr.sort()
    return arr[k-1]

def kLargest(arr, k):
    # Sort the given array arr in reverse
    # order.
    arr.sort(reverse = True)
    # Print the first kth largest elements
    return arr[k-1]




arr = [7,10,4,3,20,15]
k=3
print(kthsmallest(arr,k))
print(kLargest(arr,k))