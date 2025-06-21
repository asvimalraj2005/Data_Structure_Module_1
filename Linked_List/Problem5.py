# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    # Create a dummy node to handle edge cases like deleting the head
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == val:
            # Skip the node with value == val
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next
