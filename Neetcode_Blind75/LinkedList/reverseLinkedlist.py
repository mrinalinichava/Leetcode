class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # Use the next argument passed

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def push(self,value):
        if(not self.head):
            self.head = ListNode(value)
        else:
            temp = self.head
            while(temp):
                temp = temp.next
            temp.next = ListNode(value)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

# Building the list
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
ll = LinkedList()
ll.head = node

# Reversing and printing the list
ll.reverse()
ll.printList()
