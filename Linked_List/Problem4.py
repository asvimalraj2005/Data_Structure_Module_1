# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        # Extract values or use 0 if node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Add the two digits and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the digit
        current.next = ListNode(digit)
        current = current.next

        # Move to next nodes if available
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy_head.next
