# def check_double(list1,list2):
#     l1=[]
#     for i in list1:
#         if(2*i in list2):
#             l1.append(i)
#     return l1
# list1=[11,8,23,7,25,15]
# list2=[6,33,50,31,46,78,16,34]
# print(check_double(list1,list2))


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            while a is not None:
                if a.data ==99999:
                    pass
                else:
                    print(a.data, end=" ")
                a=a.next

    def both_traversal(self,s1,s2):
        s3 = Sll()
        n4 = Node(99999)
        s3.head = n4
        c = n4
        a=s1.head
        while a is not None:
            b = s2.head
            a1=a.data * 2
            # print(a1,"data are")
            while b is not None:
                if a1 == b.data:
                    c.next=Node(a.data)
                    c=c.next
                    # print(a.data)
                    break
                b=b.next
                a=a.next
        print("after all calculation we get final result as")
        s3.traversal()

n1=Node(11)
s1=Sll()
s2=Sll()
l1=[8,23,7,25,15]
l2=[33,50,31,46,78,16,34]
s1.head=n1
c=n1
for i in l1:
    c.next=Node(i)
    c=c.next
s1.traversal()
print()
print("second node")

#for l2
n2=Node(6)
s2.head=n2
c1=n2
for i in l2:
    c1.next=Node(i)
    c1=c1.next
s2.traversal()
print(Sll().both_traversal(s1,s2))
