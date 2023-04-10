list1=["A","app","a","d","ke","th","doc","awa"]
list2=["Y","tor","e","eps","ay",None,"le","n"]
a=0
b=len(list2)
while(a<len(list1)):
    if (list2[b-1]==None):
        list2[b-1]=''
    print(list1[a]+list2[b-1],end=' ')
    a+=1
    b-=1


