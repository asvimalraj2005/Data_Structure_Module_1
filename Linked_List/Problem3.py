# Reorder List
# Problem Description
# Given a singly linked list A
# A: A0 → A1 → … → An-1 → An 
# reorder it to:
# A0 → An → A1 → An-1 → A2 → An-2 → … 
# You must do this in-place without altering the nodes' values.
# Problem Constraints
# 1 <= |A| <= 106
# Input Format
# The first and the only argument of input contains a pointer to the head of the linked list A.
# Output Format
# Return a pointer to the head of the modified linked list.
# Example Input
# Input 1:
# A = [1, 2, 3, 4, 5] 
#Input 2:
# A = [1, 2, 3, 4] 
# Example Output
# Output 1:
# [1, 5, 2, 4, 3] 
# Output 2:
# [1, 4, 2, 3] 
# Example Explanation
# Explanation 1:
# The array will be arranged to [A0, An, A1, An-1, A2].
# Explanation 2:
# The array will be arranged to [A0, An, A1, An-1, A2].
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next or not head.next.next:
        return head
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    second = None
    while slow:
        tmp = slow.next
        slow.next = second
        second = slow
        slow = tmp
    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
    return head


