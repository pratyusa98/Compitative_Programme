
# def findFrequency(arr,n):
#     # HashMap to store frequencies
#     mp = {}
#     # traverse the array
#     for i in range(0,n):
#         # update the frequency
#         if arr[i] not in mp:
#             mp[arr[i]] = 0
#         mp[arr[i]] += 1
#         # traverse the hashmap
#     for i in mp:
#         print("Element", i, "occurs", mp[i], "times")

# arr = [2,3,2,3,5]
# n = len(arr)
#
# frequencycount(arr, n)


def frequencycount(A, N):
    for i in range(0, N):
        A[i] = A[i] - 1
    # storing the frequency of elements using mathematical formula
    for i in range(0, N):
        A[A[i] % N] = int(A[A[i] % N] + N)
    for i in range(0, N):
        A[i] = int(A[i] / N)

if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		A=[int(x) for x in input().strip().split()]
		frequencycount(A,N)
		for i in range (len (A)):
			print(A[i], end=" ")
		print()
		T-=1


