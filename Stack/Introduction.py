# Stack is an important data structure which is used to store elements in an ordered manner 
# Take a below diagram as an example for better clear understanding 
#      
#        1           <----  (5)   Top element of the stack, elements will get further added above it       
#        2           
#        3                     <---- (4) The third number is added to the stack after the second number 
#        4                     <---- (3) The second numner is added to the stack after the first number 
#        5                     <---- (2) The first number to the stack added here 
#    (1) Stack of numbers
#
#   You can add or remove elements, It you need to access the first element which is added into the stack(i.e 5 on the stack), you should have to remove the top element to bottom first element before first element and then you can able to access the first element value 5 
#   This is linear data structure where it follows the rule adding and deleting of elements in one end, simply Last In First Out as the name suggest the element that was inserted last is the first one to be taken out 
#   Stack is mostly used for recursion purposes, recursion is one of the useful concepts in competitive programming 
#   let us take a simple pythonic example 
#   where the numbers are printed from 1 to A, A is given as the input by the user 
#   Below is the python code 
#
#  
#   def PrintNumber(A):                  <-------- Process (3)
#       if A==0:                         <-------- Process (2)
#           return 1
#       else: 
#           PrintNumber(A-1)             <-------- Process (1)  
#           print(A)                     <-------- Process (4)                               
#
#   Let us take A=5                                                                 
#   PrintNumber(A)                       <-------- We are calling PrintNumber(5) function         < ==  This two lines will get executed first 
#   
#                                                                                                 Process 3                 Process 2               Process 1                            
#                                                   Let us see process (1) , (3) , (4)  ---->    PrintNumber(5)     -->       5!=0       -->     PrintNumber(5-1)    
#                                                                                                PrintNumber(4)     -->       4!=0       -->     PrintNumber(4-1)
#                                                                                                PrintNumber(3)     -->       3!=0       -->     PrintNumber(3-1)
#                                                                                                PrintNumber(2)     -->       2!=0       -->     PrintNumber(2-1)
#                                                                                                PrintNumber(1)     -->       1!=0       -->     PrintNumber(1-1)
#                                                                                                PrintNumber(0)     -->       0==0       -->     We stop here the recursion call by not entering into the else condition where there we keep on calling the function until we reach the base case 
#
#
#                                                                                                                                                
#                                                                                                                                                    
#
#                                                      On the process 1 the function calls will get stored like this  on the stack               PrintNumber(1-1) -> 0   when we reach here we exit from the call stack by printing the values from 1,2,3,4,5  ->  Now the call stack becomes like this 
#                                                      where every function call is removed from the top to bottom after getting                 PrintNumber(2-1) -> 1 
#                                                      completing its operation                                                                  PrintNumber(3-1) -> 2
#                                                                                                                                                PrintNumber(4-1) -> 3
#                                                                                                                                                PrintNumber(5-1) -> 4
#                                                                                                                                                PrintNumber(5)
#
#                                                                                                                                                PrintNumber(2-1) -> 1        1 is printed 
#                                                                                                                                                PrintNumber(3-1) -> 2
#                                                                                                                                                PrintNumber(4-1) -> 3
#                                                                                                                                                PrintNumber(5-1) -> 4
#                                                                                                                                                PrintNumber(5)                                                                                                                                              
#                                                                                                                                                
#                                                                                                                                                PrintNumber(3-1) -> 2        2 is printed 
#                                                                                                                                                PrintNumber(4-1) -> 3
#                                                                                                                                                PrintNumber(5-1) -> 4
#                                                                                                                                                PrintNumber(5)
#
#                                                                                                                                                PrintNumber(4-1) -> 3        3 is printed 
#                                                                                                                                                PrintNumber(5-1) -> 4
#                                                                                                                                                PrintNumber(5)
#                                                                                           
#                                                                                                                                                PrintNumber(5-1) -> 4        4 is printed 
#                                                                                                                                                PrintNumber(5)
#                                                                                                                                       
#                                                                                From below the call stack is gets constructed                   PrintNumber(5)   -> 5        5 is printed 
#                                                                                just a note 
#
#
#

