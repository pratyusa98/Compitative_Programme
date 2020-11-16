import array as arr


a = arr.array('i',[])
n= int(input("number of element insert"))

for i in range(0,n):
    index = int(input("index"))
    inpu = int(input("value"))

    a.insert(index,inpu)

for j in (a):
    print (j, end =" ")
print()
