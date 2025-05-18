# Problem Statement 
# Single Element 2 ( Every element 3 times will occur in the array sequentially where one element is unique from those find the unique element in the array )
# Example 1 let us take an array named A = [ 2 , 2 , 2 , 3 , 3 , 3 , 4 , 5 , 5 , 5 , 6 , 6 , 6 ]
# From the observation in the A array we can see 2 , 3 , 5 , 6 will be occurring thrice the times while only 4 occurred once 
# So four is the answer, and return four 
# Input Format : First and only argument of input contains an integer array A 
# Output Format : Return a single integer 
# Problem Solution Approach 
# By using count function and passing the array element into the count function and checking the if array element present once then we return if not return 0 
# Below is the python for the above line statement 
def FindtheUnique(A):
    countValue=1                         # Already defining the variable named count with value with one so it is easy  to check whether we are inside the loop and if condition 
    for element in A:                    # Iterating over the elements in A by using the iteration variable element we can use any variable and different loop approach for accessing the elements inside the array 
        if A.count(element)==countValue: # A.count(element)==countValue : This says that for every sequentialised or non sequential elements which present in the list A will be checked thrice and anyone of the element which present once in the A list and satisfies the if condition 
            return element               # Then we are returning the element  
    return None

A=[2,2,2,3,3,3,4,5,5,5,6,6,6]               # Defining the values for the array or an list A
Result=FindtheUnique(A)                     # Passing the value into the function and storing the returned value in here 

# The above approach uses simple count function and counts the element present inside the List A, condition check returns etc 
# Now we are moving to the Bit Manipulation Approach 
# Previously we have used XOR for the calculation of finding the unique element where every element appears twice , XOR cancel out same bits --> A^A=0
# If count of set bits at the position is equal to 2 then output is zero 
# A = 10       8 4 2 1                                         
#              1 0 1 0   ->  A ^ A = 1 0 1 0 ^ 1 0 1 0 = 0 0 0 0        Multiple of 2 -> 1 1 
# But in here the elements are appearing thrice 
# Let's take an example List Arr= [ 5 , 7 , 5 , 4 , 7 , 11 , 11 , 9 , 11 , 7 , 5 , 4 , 4 ]
# Binary Representatin of 
# all the elements         
#                       5 -->      0   1   0   1 
#                       7 -->      0   1   1   1
#                       5 -->      0   1   0   1 
#                       4 -->      0   1   0   0 
#                       7 -->      0   1   1   1
#                      11 -->      1   0   1   1
#                      11 -->      1   0   1   1
#                       9 -->      1   0   0   1
#                      11 -->      1   0   1   1
#                       7 -->      0   1   1   1
#                       5 -->      0   1   0   1
#                       4 -->      0   1   0   0
#                       4 -->      0   1   0   0 
#     Count of ones 
#     Bit's at 0 th position                   10    (Skip this line)  Now the elements which are present inside the list have the triplet of set bit at this position then we can tell this is a multiple of 3 , then this is not the answer 
#     Bit's at 1 th position               6         (Skip this line too ) 6 sets at postion 1 it is a multiple of 3 which means where the number are in triplet will have this position bit as set 
#     Bit's at 2 nd position           9
#     Bit's at 3 rd position       4              
#
#     Count of ones gives us the idea about the solution, the postion where the multiple of 3 is present  i.e   4 , 9 , 6 , 10  --> 9 is a multiple of 3 and 6 is the multiple of 3  --> multiples of 3 will become zero and non-multiples of 3 will become one 
#     4  6  9  10  
#        0  0             <---  Multiple of three will become zero 
#     1         1         <---  Non-Multiple of three will become one
#  Now  after getting the number as 1 0 0 1 we are converting to it's integer value 8 4 2 1
#                                                                                   1 0 0 1  --> 9 
# (Skip this line too) if should be multiple of 3 for the answer this bit is unset 
# Recap --> Count of set bits 1) If Multiple of 3 --> Unset the bit in ans 
#                             2) If not Multiple of 3 --> Set the bit in ans 
# Below is the python code for the above approach 
def CountUniqueFromThrice(A):
    ans=0
    N=len(A)
    for i in range(32):                                         # Executing the Loop from 1 to 32 for the bit range                          i
        counter_variable=0                                      # Used to count the sets bit in the position of 'i'      i.e        8  4  2  1 
        for j in range(N):                                      # Running a loop till the end length of the List A                                                     
            if (A[j]&(1<<i))>0:                                 # If the integer binary representation is set at the postion j 
                counter_variable=counter_variable+1             # Then counter_variable will increment by 1 
        if counter_variable % 3 != 0:                           # Not a mulitple of 3 then if condition is used to set the bit 
            ans |=(1<<i)                                        # For to set the bit inside the answer we are using OR with LEFT SHIFT operator and i variable for position to get set 
    return ans  
        
A=[5,5,5,6,7,7,7]
print(CountUniqueFromThrice(A))
            