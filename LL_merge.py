'''Write a python function which accepts two linked lists containing integer data and an integer, n and merges the two linked lists, such that list2 is merged with listi after n number of nodes.

Assume that value of n will always be less than or equal to the number of nodes in listi.

Sample Input Expected Output,

listi

1->2->4->3->5

list2- 9-8->11

n- 2 1->2-9-8->11->4->3->5'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(list1, list2, n):
    if not list1:
        return list2

    curr = list1
    count = 1

    while curr.next and count < n:
        curr = curr.next
        count += 1

    temp = curr.next
    curr.next = list2

    while list2.next:
        list2 = list2.next

    list2.next = temp

    return list1


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(5)


list2 = ListNode(9)
list2.next = ListNode(8)
list2.next.next = ListNode(11)

result = merge_lists(list1, list2, 2)

while result:
    print(result.val, end=',')
    result = result.next
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(1)
# n1.next=Node(2)
# n1.next.next=Node(4)
# for i in n1:
#     print(i.data)