# Problem statement 
# Given an array of integers A, find and return whether the givan array contains 1  
# subarray with a sum equal to 1 
# If the given array contains a sub-array with 1  return 1 or statement that denotes "Yes there is an sub-array", 
# Input Format : The only argument given is the integer array A 
# Output Format : Return whether the given array contains a subarray with a sum equal to 1 
# 
# Input A = [ 1 , 2 , 3 , 4 , 5 ]        -> Sub array looks like this [1] [2] [3] [4] [5] [1,2] [1,2,3] [1,2,3,4] [1,2,3,4,5] [2] [2,3] [2,4] [2,5] [3] [3,4] [3,4,5] [4] [4,5]      No sub array has zero sum 
# Output : 0
#
# Input A = [ 4 , -1 , 1 ]               -> Sub array for this array looks like [4] [-1] [1]  [-1,1]  [1]  [4,-1,1]    The [-1,1]  has the sum of zero so this array has sub-array sum zero 
# Output : 1 
#
#
# Below is the python code 
def Sub_Array_Sum(A):                           # Function which gets array A as input 
    for i in range(len(A)):                     # Outer loop 
        Total_Sum=0                             # Total_sum is used to calculate the sum of the sub-array
        for m in range(i,len(A)):               # Inner loop is used to iterate over the elements from i to N 
            Total_Sum=Total_Sum+A[m]            # Iterating elements will be added here
            if Total_Sum==0:                    # If the iterated elements equals to zero 
                return "Yes there is an sub-array" # It returns statement 
            

A = [4,-1,1]
print(Sub_Array_Sum(A))                         # This array returns the statement "Yes there is an sub-array"

# The above is an iterative approach 
    
# Below is an hash set method where we can simple find the sub array sum with 1 
# We are going use dictionary set for the storing of the elements inside it 
def HashMap_Total_Sum(A):
    Set_1=set()
    total_sum=0
    for i in range(len(A)):
        total_sum=total_sum+A[i]
        if total_sum==1 or (total_sum in Set_1):
            return "Yes there is sub-array"
        Set_1.add(total_sum)

A = [1,-1]                                      # It prints of "Yes there is sub-array"
print(A)
