# Linked list is an python data structure where it is divided into three types, single linked list, doubly linked list and circular linked list 
# Single linked list -> data and node address, the address of the node is connected to the next node
# Doubly linked list -> data and node address, the address of the current node is pointed in both of the direction, where we can go back and forth while traversion around them
# Circular linked list -> data and node address, same as doubly linked list where the last node of the circular linked list is connected to the first node of the cicular linked list 
# Operations inside a linked list : 
#                     __init__ -> Creates an empty head in the linked list 
#                     BeginInsertion() -> Inserts a node at the beginning of the linked list 
#                     EndInsertion() -> Inserts a node at the end of the linked list 
#                     Remove_Operation() -> Removes a node in the linked list
#                     Size() -> Returns the length of the linked list 
#                     PrintLinkedList() -> Traverses over the linked list and prints all the linked list data present inside them 
# 
# Python code for creating a head node
#
# class Node :                                  # Whenever a new object is created with different names like obj1,obj2 by using the name of 'Node' 
#       def __init__(self,data):                # Head is created as a object where this object should be connected with the linked list nodes 
#               self.data=data                  # The head node consist of data and next none pointer
#               self.next=None                  
#  
#
# Python code for inserting the head node with data and next None pointer to the linked list nodes 
# 
# def BeginInsertion(self,data):                # Head node with data is passed in this function through the function call
#       new_node=Node(data)                     # New node is created under the name of new_node with the data consisting init 
#       if self.head is None:                   # If the linked list doesn't even consist of any node i.e blank data structure
#           self.head = new_node                # assigning the new_node with data and next pointer none as the head node
#           return                              # After creating a structure we are exiting from the data structure 
#       else:                                   # If the linked list is consisted of a head node  
#           new_node.next=self.head             # then new_node is pointed to the head node 
#           self.head=new_node                  # assigning the new_node as the head node 
#
#
# Python code to delete the first node in the linked list 
#   
# def remove_first_node(self):                  # This function is used to remove the first node in the linked list 
#       if(self.head==None):                    # If the head node is None
#           return                              # We are retuning or exiting from the data structure
#       self.head=self.head.next                # assigning the head node pointer to the next node from the previously deleted node 
#
# 
# Python code for to insert a node at the end of the linked list
#
# def EndInsertion(self,data):                  # This function is used to insert a node at the end of the list 
#       new_node=Node(data)                     # New node is created under the name of 'new_node' with data
#       if self.head is None:                   # If head node is not there in the linked list   
#           self.head = new_node                # self.node is assigned with the node of new_node
#           return                              # Exiting out from the function
#       current_node = self.head                # current_node is consisted of the head node pointer not to affect the original linked list pointers 
#       while(current_node.next):               # Iterating over the node by using the  current_node by using the 'next' pointer, until we reach the current_node next pointer is None
#           current_node=current_node.next      # Iterating through the end
#       current_node.next=new_node              # After reaching the end of the linked list, we are assigning the current_node next pointer to the new_node 
#
#
# Python code for to remove a node at the end of the linked list 
#
# def remove_last_node(self):                   # Removing the last node of the linked list 
#       if self.head is None:                   # If the linked list is None
#           return                              # The function call is exiting out from the linked list 
#       curr_node = self.head                   # Assigning the self.head pointer to the curr_node 
#       while(curr_node.next !=None and curr_node.next.next!=None):      # Reaching the node where the curr_node next is not becomes None 
#           curr_node=curr_node.next            # Iterating 
#       curr_node.next=None                     # Removing the last node by modifying the curr_node.next to curr_node.next = None 
#
# 
