class Queue:                                                                                #FIFO
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.rear=-1
        self.front=0
    def is_full(self):
        if(self.rear==self.max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.front > self.rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
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
        for index in range(self.front,self.rear+1):
            print(self.element[index])
    def get_maxsize(self):
        return self.max_size
q= Queue(5)
print(" is it full",q.is_full())
print("is it empty",q.is_empty())
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.enqueue(400)
q.enqueue(500)
print("Deleted element is:",q.dequeue())
q.display()
