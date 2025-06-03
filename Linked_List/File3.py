<<<<<<< HEAD
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
=======
# Remove every i-th node of the linked list 
# Here is an example 1>2>3>4>5>6
# i=2 
# 1>2>3>4>5>6
# 1 2 1 2 1 2  -> 2nd index positioned elements will always get removed and the 1st index positioned will get printed while in the process of printing 
# i=3
# 1>2>3>4>5>6>7>8>9>10
# i=3 
# 1>2>3>4>5>6>7>8>9>10
# 1 2 3 1 2 3 1 2 3 1 
# Every 1 and 2 index positioned node will get printed but the ones who has index positioned as 3 will not get printed while in the process of printing 
# Below is the python code for the above problem statement 
class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
class LL:      
        def __init__(self):
            self.head=None
        def EndInsertion(self,data):                # This function is used to insert a node at the end of the list 
            new_node=Node(data)                     # New node is created under the name of 'new_node' with data
            if self.head is None:                   # If head node is not there in the linked list   
                self.head = new_node                # self.node is assigned with the node of new_node
                return                              # Exiting out from the function
            current_node = self.head                # current_node is consisted of the head node pointer not to affect the original linked list pointers 
            while(current_node.next):               # Iterating over the node by using the  current_node by using the 'next' pointer, until we reach the current_node next pointer is None
                current_node=current_node.next      # Iterating through the end
            current_node.next=new_node              # After reaching the end of the linked list, we are assigning the current_node next pointer to the new_node 

# The below code is to add node to the end of the linked list 
# Now comes the hard part after adding n no of elements to it we need to print without the i-th element while printing not by removing them 
# Let us take i=5, count=1 ; now while printing an single node we should increment the count by one, if the count reaches 4 then we should skip the next node element on the linked list and re-initialize the count to 1 and so on 
# Below is the code for the above approach 
        def printNodes(self,i):
            count=1         # for every count we be skipping an element 
            curr=self.head
            while(curr.next):
                if count%i!=0:                  # Skipping every i-th node 
                    print(curr.data)
                count=count+1
                curr=curr.next

l1=LL()
for n in range(1,11):
    l1.EndInsertion(n)

print("Skipping every 2nd node")
l1.printNodes(3)
        
            
            
>>>>>>> 6ac5612 (Linked List)
