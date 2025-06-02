# Program to search an value inside the linked list present or not 
# If the given element is present inside the linked list we be returning the True if not False 
# Below is the program for the above program
#
class Node:
    def __init__(self,data):                 # <-- Constructor that initialize node with data  
        self.data=data
        self.next=None 

def Search(head,y):                          # <-- y is the element where it should be searched in the linked list 
    curr=head                                # <-- Assigning the head node to the curr for not modifying the original linked list pointers 
    while curr is not None:                  # <-- while loop traverses until the current node next pointer not becomes None
        if curr.data==y:                     # <-- If the current node data is equals to y value then we are returning the True value 
            return True                      # <-- Exiting the function and by returning True
        curr=curr.next                       # <-- Pointer to move from one node to next node 
    return False                             # <-- If the y element is not present then we are returning False 
#
# Below is the code for insertion of elements in the linked list 
head=Node(3)
head.next=Node(4)
head.next.next=Node(5)
head.next.next.next=Node(6)
head.next.next.next.next=Node(7)
head.next.next.next.next.next=Node(8)
y=14
if Search(head,y):
    print("Yes")
else:
    print("No")