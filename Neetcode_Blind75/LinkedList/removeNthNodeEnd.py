class ListNode:
    def __init__(self,val = 0, next=None):
        self.val = val
        self.next = next


def removeNthNodeFromEnd(head,n):

    length = 0
    temp = head
    while(temp.next):
        length = length+1
        temp = temp.next
    temp = head
    required = length - n + 1
    print(required)
    for i in range(required):
        prev = temp
        temp = temp.next

    if(prev==None):
        return head.next
    else:
        prev.next = prev.next.next
    return head

def printList(node):
    temp = node
    while(temp):
        print(temp.val,end= "->")
        temp = temp.next

node = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))

printList(removeNthNodeFromEnd(node,3))