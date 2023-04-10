class Stack:                                                                            #LIFO
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if (self.__top== self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if (self.is_full()):
            print("Stack is Full")
        else:
            self.__top+=1
            self.__element[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("Stack Empty")
        else:
            data=self.__element[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("Stack Empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__element[index])
                index-=1
    def get_maxsize(self):
        return self.__max_size
s= Stack(4)
print("is it empty",s.is_empty())
s.push(5)
print("is it empty",s.is_empty())
s.push(6)
s.push(7)
s.push(8)
s.pop()
s.display()
print("SIze of the Stack is:",s.get_maxsize())
