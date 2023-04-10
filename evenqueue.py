class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.elements=[]
        self.front=-0
        self.rear=-1
    def is_full(self):
        if(self.rear == self.max_size-1):
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
            self.rear += 1
            self.element[self.rear] = data
    def dele_element(self,data):
        self.elements.remove(data)
        return self.elements
    def display(self):
        for i in self.elements:
            print(i,end=' ')
    def check_even(self):
        self.elements=self.element
        for i in range(1,11):
            for index in self.elements:
                if(index%i!=0):
                    q.dele_element(index)

q=Queue(5)
q.enqueue(13983)
q.enqueue(10080)
q.enqueue(7113)
q.enqueue(2520)
q.enqueue(2500)
q.check_even()
q.display()






