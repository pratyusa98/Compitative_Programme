"""
Input : arr[] = {100, 10, 5, 25, 35, 14},
            n = 11
Output : 9
100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
"""

def mul(arr):
    result = 1
    for i in arr:
        result = result*i
    return result

arr = [100,10,5,25,35,14]
n=11

a = mul(arr)
print(a % 11)
