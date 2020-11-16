"""
Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
"""


arr = [20, 10, 20, 4, 100]

max =arr[0]

for i in range(0,len(arr)):
    if arr[i]>max:
        max = arr[i]
print(max)
