
## Craete an array
import array as arr

a = arr.array("i",[1,2,3,4,5])
for i in a:
    print(i,end=" ")
print()
##sum array
print("sum is: ",sum(a))
## substaration
def sub(a):
    result = 0
    for i in a:
        result = i-result
    return result
print("substract is :",sub(a))
##multiplication
def mul(a):
    result = 1
    for i in a:
        result = i*result
    return result
print("multiplication is: ",mul(a))