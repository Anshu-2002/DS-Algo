class Queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.element=[None]*self.maxsize
        self.front=0
        self.rear=-1
    def enqueue(self,data):
            self.rear+=1
            self.element[self.rear]=data
    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.element[index],end=" ")
    def even1(self,list1):
        for i in list1:
            if i%2==0:
                even.enqueue(i)
            else:
                odd.enqueue(i)
even=Queue(10)
odd=Queue(10)
list1=list(map(int,input().split(",")))
q=Queue(10)
q.even1(list1)
even.display()
print()
odd.display()