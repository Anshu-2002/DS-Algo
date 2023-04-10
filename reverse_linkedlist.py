class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,dataval):
        new=Node(dataval)
        new.next=self.head
        self.head=new
    def display(self):
        printval=self.head
        while printval is not None:
            print(printval.data,end=' ')
            printval=printval.next
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next= prev
            prev = current
            current=next
        self.head= prev
l1=Linkedlist()
# l1.head = Node("Sun")
# e1=Node("Mon")
# e2=Node("Tues")
# e3=Node("Wed")
# l1.head.next=e1
# e1.next=e2
# e2.next=e3
l1.insert("Mon")
l1.insert("Tues")
l1.insert("Wed")
l1.insert("Thurs")
l1.insert("Fri")
l1.display()
print()
l1.reverse()
l1.display()