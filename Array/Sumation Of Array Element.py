"""
Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6

Input : arr[] = {15, 12, 13, 10}
Output : 50
"""

arr = []
arr = [15,12,13,10]
# result = sum(arr)
# print(result)

sum = 0
for i in arr:
    sum = sum+i
print(sum)