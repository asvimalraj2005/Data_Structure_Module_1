# Problem Statement
# Print Array Using Recursion 
# You are given an array A. Print the elements of the array using recursion
# Note : You are required to not use any loops, You can create new functions.
#        Don't change the signature of the function PrintArray 
#        Print a new empty line after printing the output 
# Below is the python code for the above problem statement 
# For to access the element inside the given array we should use index variable and increment by 1 until we reach the Length of the array 
# Skip the below approach and code 
def PrintArray(A):
    N=len(A)
    Index_Variable_Iterator=0                           # For every function call this variable resets to zero , if the signature of function can be changeable than it's easy to implement the code with out any errors or worry 
    if N==0 or Index_Variable_Iterator==N :
        return 
    else: 
        
        print(A[0])
        Index_Variable_Iterator = Index_Variable_Iterator + 1
        PrintArray(A)
        

A=['1','2','3','4','5','6','7','8','9'] 
PrintArray(A) 


# The above method is my own approach but due to some syntatical error I couldn't able to properly implement the code 
# Below is another where I am using two functions one is signature function without using changing the already defined structure of it i.e PrintArray(A)
# And the second function is used to pass the array and index for printing the array elements 
#
#
def PrintArray(A):                  # Main Signature Function : only Argument passed here is array A or List A 
    def helper(index):              # Using a helper function within inside the PrintArray function for indexing purpose where the indexes are helpful for accessing the array elements 
        if index==len(A):           # Base case condition if 'index' variable == len (A)  we are returned back to the original function 
            return 
        print(A[index],end=' ')     # Until then we are printing the array elements 
        helper(index+1)             # Calling the helper function again and again for the index to get incremented
    helper(0)                       # We should to define the index as 0 when we are going to call the helper function inside the PrintArray function 
    

A=['8','7','6','5','4','3','2','1']
PrintArray(A)

# Approach three where the element is removed before getting removed it got printed with the help of the recursion 
def PrintArray(A):
    if len(A)==0:
        return 
    else:
        Index_0_th_Element=0
        print(A[0])
        A.pop(0)
        PrintArray(A)

A=['1','2','3','4','5','6','7']
PrintArray(A)


    