def Selction_sort(array):
    length = len(array)
    for i in range(length-1):
        minimum = i
        for j in range(i+1,length):
            if array[j] < array[minimum]:
                minimum = j
        array[i],array[minimum] = array[minimum],array[i]
    return array
# l1=[20,12,10,15,2]
l1=list(map(int,input().split(",")))
print(Selction_sort(l1))