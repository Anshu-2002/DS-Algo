class node:
    def __init__(self, value):                                              #361
        self.prev = None
        self.data = value
        self.next = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def insert_begining(self, value):
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, value):
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
    #
    # def insert_middle(self, prev_node, value):
    #     new_node = node(value)
    #     if prev_node is None:
    #         return False
    #     temp = prev_node.next
    #     new_node.prev = prev_node
    #     new_node.next = temp
    #     prev_node.next = new_node
    #     temp.prev = new_node
    def insert_at_position(self,value,position):
        temp=self.head
        count = 1
        while temp is not None:
            if count == position-1:
                break
            count+=1
            temp=temp.next
        if position ==1:
            self.insert_begining(value)
        elif temp is None:
            print("There are less than ")
        elif temp.next is None:
            self.insert_last(value)
        else:
            new=node(value)
            new.next=temp.next
            new.previous=temp
            temp.next.previous = new
            temp.next = new
    def deleteFromPosition(self,position):
        if self.is_empty():
            print("empty")
        elif position ==-1:
            self.deleteFromBegining()
        else:
            temp = self.head
            count=1
            while temp is not None:
                if count == position:
                    break
                temp=temp.next
                count=count+1
            if temp is not None:
                print("can`t delete element")
            elif temp.next is not None:
                self.deletefromlast()

    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=' ')
            temp = temp.next


list1 = doubly_linked_list()
list1.head = node(23)
e2 = node(25)
e3 = node(33)
list1.head.next = e2
e2.next = e3
list1.insert_begining(3)
list1.insert_begining(4)
list1.insert_begining(5)
list1.insert_begining(6)
list1.insert_begining(8)
list1.print_linked_list()
print()
list1.insert_last(12)
list1.print_linked_list()
print()
list1.insert_at_position(4,22)
#list1.insert_middle(e2, 22)
list1.print_linked_list()
print()
print(list1.length())