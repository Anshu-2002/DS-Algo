class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def push(self,data):
        new = Node(data)
        new.next=self.head
        self.head=new
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data , end=' ')
            temp= temp.next
    def duplicate(self):
        temp=self.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                temp.next =temp.next.next
            else:
                temp=temp.next
        return temp
l1=LL()
l1.head= Node(10)
n2=Node(10)
n3= Node(20)
n4=Node(20)
n5=Node(30)
n6=Node(30)
n7=Node(40)
n8=Node(50)
l1.head.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8
l1.printlist()
print()
l1.duplicate()
l1.printlist()
