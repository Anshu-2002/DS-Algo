#Linked List Implementation
class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval,end=' ')
            printval = printval.nextval
    def At_begining(self,newdata):
        newnode=Node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode
    def in_between(self,prev_node,new_node):
        if (prev_node==None):
            print("The mentioned node is absent")
        new_node=Node(new_node)
        new_node.nextval = prev_node.nextval
        prev_node.nextval = new_node
    def At_end(self,newdata):
        newnode=Node(newdata)
        if(self.headval == None):
            self.headval=newnode
            return
        last=self.headval
        while(last.nextval):
            last=last.nextval
        last.nextval= newnode
    def del_at_first(self):
        if self.headval is None:
            return False
        self.headval=self.headval.nextval
    def del_at_last(self):
        if self.headval is None:
            return False
        last=self.headval
        while last.nextval.nextval is not None:
            last=last.nextval
        last.nextval=None



list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
list1.At_begining('Sun')
list1.in_between(e4,'Fri')
list1.At_end("Sat")
list1.listprint()