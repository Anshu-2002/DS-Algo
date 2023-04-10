def partition(array,low,high):
    pivot = array[high]
    i= low-1
    for j in range(low,high):
        if array[j]<= pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1
def quicksort(array,low,high):
    if low <high:
        p=partition(array,low,high)
        quicksort(array,low,p-1)
        quicksort(array,p+1,high)
# data = [8,7,6,1,0,9,2]
data = [10,80,30,90,40,50,70]
quicksort(data,0,len(data)-1)
print(data)