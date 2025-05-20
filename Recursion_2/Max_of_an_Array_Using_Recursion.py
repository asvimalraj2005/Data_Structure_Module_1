# Problem Description 
# Given an array A of size N, write a recursive function that returns the maximum element of the array 
# The first line contains the Array A 
# A single integer is the maximum value of the array 
# Example Input : A = [ 12 , 10 , 3 , 4 , 5 ]
# Example Output : 12 
# Example Explanation : The Maximum element of the array A = [ 12 , 10 , 3 , 4 , 5 ] is 12 
# Approach one without recursion but by using python max function 
# Approach two using an loop with first element stored into an variable and iterating over the array elements if any elements found greater than the element[0] then we should update the variable element [0] with the found greater element 
# Approach three using recursion approach and an helper function inside it 
# Below is the python code for the recursion approach 
def Max_Element_Recursion(A):                               # Main function
    def Helper(A,Index_Element,First_Element):              # Helper function is used to Array A, Index_Element -> Indexes over the array, First_Element <- where first element is usually stored 
        if Index_Element==len(A):                           # Base Case return condition 
            return First_Element                            # Returning the first element if the first is larger or in where the first element is positive and other elements are negative in the array 
        elif A[Index_Element]>First_Element:                # Updating happens here where if the next element is greater than the FirstElement then the FirstElement value will get updated 
            First_Element=A[Index_Element]                  # Assigning 
        return Helper(A,Index_Element+1,First_Element)      # Recursive call within the fucntion after every call the returned value of this Helper function will get forwarded to the main function 
    return Helper(A,0,A[0])                                 # The main function gets the value here and return over to the global space where the user uses an variable for calling and printing the max of the array 


A=[1,2,3,4,5,44,3,2,1,8,6]
print(Max_Element_Recursion(A))