def binary_search(array,x,high,low):
    while low<=high:
        mid = (low+high)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high = mid-1
    return -1
array=[1,2,3,4,5,6]
x=7
res= binary_search(array,x,len(array)-1,0)
if res==-1:
    print("Not Found")
else:
    print("Index of the search element is:",res)

