# Middle element of linked list
# Problem Description
# Given a linked list of integers, find and return the middle element of the linked list.
# NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
# Problem Constraints
# 1 <= length of the linked list <= 100000
# 1 <= Node value <= 109
# Input Format
# The only argument given head pointer of linked list.
# Output Format
# Return the middle element of the linked list.
# Example Input
# Input 1:
# 1 -> 2 -> 3 -> 4 -> 5
# Input 2:
# 1 -> 5 -> 6 -> 2 -> 3 -> 4
# Example Output
# Output 1:
# 3
# Output 2:
# 2
# Example Explanation
# Explanation 1:
# The middle element is 3.
# Explanation 2:
# The middle element in even length linked list of length N is ((N/2) + 1)th element which is 2.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def findlength(self,head):
        count = 0
        
        temp = head 
        while temp:
            temp = temp.next
            count += 1
            
        return count

    def solve(self, A):
        if not A or not A.next:
            return A
        
        N = self.findlength(A)
        
        to_find = (N//2) 
        
        temp = A
        while to_find != 0:
            temp = temp.next
            to_find -= 1
            
        return temp.val


        # optimized  - floyd's hare
        slow = A 
        fast = A 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 


        return slow.val

