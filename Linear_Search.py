#Linear Search on Python
def Linearsearch(array,n,x):
    for i in range(0,n):
        if (array[i]==x):
            return i+1
    return -1
array =[2,4,0,1,9]
x=1
n=len(array)
res = Linearsearch(array,n,x)
if (res == -1):
    print("Element Not Found")
else:
    print("Found at position:",res)