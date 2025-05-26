# Stack operations --> push() , pop() , top() , isEmpty() , size()
# push()      --> push() operation is used insert an element into the stack
# pop()       --> to remove an element from the stack
# top()       --> returns the top element of the stack 
# isEmpty()   --> returns True if the stack is empty else False 
# size()      --> returns the size of the stack 
#
#
Stack = [1,2,3,4,5] 
print("Original Stack is : ",Stack)
#
# Now the original stack will be printed like this [ 1 , 2 , 3 , 4 , 5 ]
#
#
Stack.append(7)                                   
print("Stack after push operation is :",Stack)    #  -->  [ 1 , 2 , 3 ,4 , 5 , 6 , 7 ]
#
#
Stack.pop()
print("Stack after pop operation is",Stack)       #  -->  Returns the first element of the stack 
#
#
last_element_index=len(Stack)-1                   #  -->  Array is used here for the purpose of stack convention so for to access the first element inside the stack we are using the len method of list for to find the length of the list and accessing the last element by subtracting the got value by 1 
print("value obtained after the pop operation is",Stack[last_element_index])
#
#
#
# Below is the program to print the top element of the stack by using function method named topElement()
#
#
def topElement(A):
    return A[-1]
#
#
S=[]                       # Stack is created here
S.append(10)               # Pushing operation is done where the stack contains 10 inside it 
print(topElement(S))       # Printing the top element of the stack by passing the stack S into the function topElement(A)
#                                                                                                                            20       <-- Top
S.append(20)               # List convention of stack the last element is the first element of the stack     Stack S be like 10       <-- Bottom of the stack
#
print(topElement(S))       # Top of the stack element will gets printed here     
#

