class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Replace:
    def __init__(self):
        self.head = None
        self.maximum = None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    def get_max(self):
        current = self.head
        self.maximum = self.head.data
        while current is not None:
            if (self.maximum < current.data):
                self.maximum = current.data
            current = current.next
        return self.maximum
    def replace_value(self,n):
        while self.head is not None:
            if self.head.data == self.maximum:
                self.head.data = n
            print(self.head.data,end=" ")
            self.head = self.head.next

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
R=Replace()
R.push(12)
R.push(95)
R.push(140)
R.push(110)
R.push(40)
R.printlist()
print()
n=int(input("Enter your desired number to display: "))
print("Maximum value present is \n",R.get_max())
R.replace_value(n)
R.printlist()



