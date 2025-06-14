# Merge Two Sorted Lists
# Problem Description
# Merge two sorted linked lists, A and B, and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists and should also be sorted.
# Problem Constraints
# 0 <= |A|, |B| <= 105
# Input Format
# The first argument of input contains a pointer to the head of linked list A.
# The second argument of input contains a pointer to the head of linked list B.
# Output Format
# Return a pointer to the head of the merged linked list.
# Example Input
# Input 1:
# A = 5 -> 8 -> 20
# B = 4 -> 11 -> 15
# Input 2:
#  A = 1 -> 2 -> 3
#  B = Null
# Example Output
# Output 1:
#  4 -> 5 -> 8 -> 11 -> 15 -> 20
# Output 2:
# 1 -> 2 -> 3
# Example Explanation
# Explanation 1:
# Merging A and B will result in 4 -> 5 -> 8 -> 11 -> 15 -> 20 
# Explanation 2:
# We don't need to merge as B is empty. 
# Below is the code for the above problem
class Solution:
	def mergeTwoLists(self, list1, list2):
            if not list1: 
                return list2
            if not list2: 
                return list1
            if not list1 and list2: 
                return None
        
            head = None
            if list1.val < list2.val: 
                head  = list1 
                list1 = list1.next
            else:
                head  = list2
                list2 = list2.next
            
            tail = head
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                
                tail = tail.next
            
            
        
            if list1: 
                tail.next = list1
            else: 
                tail.next = list2
            
            
            return head
