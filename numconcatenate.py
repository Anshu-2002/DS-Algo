class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.front=0
        self.rear=-1
    def is_full(self):
        if(self.rear==self.max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.front>self.rear):
            return True
        return False
    def enqueue(self,data):
        if (self.is_full()):
            print("full")
        else:
            self.rear+=1
            self.element[self.rear]=data
    def dequeue(self):
        if (self.is_empty()):
            print("Queue is empty")
        else:
            data=self.element[self.front]
            self.front+=1
            return data
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.element[i],end='')

q=Queue(5)
q.enqueue(3)
q.enqueue(6)
q.enqueue(8)
q2=Queue(10)
q2.enqueue('b')
q2.enqueue('y')
q2.enqueue('u')
q2.enqueue('t')
q2.enqueue('r')
q2.enqueue('o')
q3=Queue(15)
q.display()
q2.display()
print()
while(not q.is_empty() or not q2.is_empty()):

    if(q.is_empty()):
        q3.enqueue(q2.dequeue())
    elif(q2.is_empty()):
        q3.enqueue(q.dequeue())
    else:
        q3.enqueue(q.dequeue())
        q3.enqueue(q2.dequeue())

q3.display()