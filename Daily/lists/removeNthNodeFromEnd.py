# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to convert a list to a linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Function to convert a linked list to a list (for easy comparison)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Function to print the linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


# The removeNthFromEnd function
def removeNthFromEnd(head, n):
    left = right = head
    prev = None

    # Move right pointer n steps ahead
    for i in range(n):
        right = right.next

    # Traverse the list with both pointers until right reaches the end
    while right:
        prev = left
        left = left.next
        right = right.next

    # If prev is None, it means we need to remove the head node
    if prev is None:
        return head.next

    # Remove the N-th node from the end
    prev.next = prev.next.next

    return head


# Test cases
def test_remove_nth_from_end():
    # Test case 1: Removing the 2nd node from end in [1, 2, 3, 4, 5]
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original list: ")
    print_linked_list(head)
    new_head = removeNthFromEnd(head, 2)
    print("After removing 2nd node from the end: ")
    print_linked_list(new_head)
    assert linked_list_to_list(new_head) == [1, 2, 3, 5], "Test case 1 failed"

    # Test case 2: Removing the 1st node from end in [1]
    head = create_linked_list([1])
    print("Original list: ")
    print_linked_list(head)
    new_head = removeNthFromEnd(head, 1)
    print("After removing 1st node from the end: ")
    print_linked_list(new_head)
    assert linked_list_to_list(new_head) == [], "Test case 2 failed"

    # Test case 3: Removing the 1st node from end in [1, 2]
    head = create_linked_list([1, 2])
    print("Original list: ")
    print_linked_list(head)
    new_head = removeNthFromEnd(head, 1)
    print("After removing 1st node from the end: ")
    print_linked_list(new_head)
    assert linked_list_to_list(new_head) == [1], "Test case 3 failed"

    # Test case 4: Removing the head node (2nd from end) in [1, 2]
    head = create_linked_list([1, 2])
    print("Original list: ")
    print_linked_list(head)
    new_head = removeNthFromEnd(head, 2)
    print("After removing 2nd node from the end (the head): ")
    print_linked_list(new_head)
    assert linked_list_to_list(new_head) == [2], "Test case 4 failed"

    print("All test cases passed!")


# Run the test function
test_remove_nth_from_end()
