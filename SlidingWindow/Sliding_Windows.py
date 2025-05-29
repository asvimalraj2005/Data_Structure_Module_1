<<<<<<< HEAD
# Subarray : Continuoes part of array 
# 1 2 3 4 5 
# {2,3}  wrong
# 2 4 1 6 -3 7 8 4 
# 1 6 8 
# 1 4 
# 6 1 4 2 
# 7 8 4 
# No of subarrays = N * ( N + 1 ) / 2 
# for i in range(len(A))
#   for j in range(i,len(i)):
#       for k in range(i,len(A)):
# 
# Given an array find the sum of all subarray
# Example array = {3,2,5}
#               --> 3
#               --> 3 2 
#               --> 3 2 5 
#               --> 2 
#               --> 2 5 
#               --> 5 
# 
# Direct approach
# for each subarray, Iterate and get the sum 
# Below is the code for the above approach
def Subarray(A):
    ans=0
    for s in range(len(A)):                                # s iteration element travels all the elements in the sub array 
        for u in range(len(A)):                            # for every s, u travels along with it 
            sum=0                                          # To process the sum of the sub-array we are using sum variable to store the sum of the sub-array 
            for b in range(u+1):                           # This loop is used to iterate all the elements in the sub-array 
                sum=sum+A[b]                               # Summing the elements 
            ans=ans+sum                                    # After processing the sum of the current sub-array, we are appending the progressed sum to the next sub-array sum calculation 
    return ans                                             # Returning the overall sum to the main function 
# But the above approach time complexity is O(n^3)
# and process the sum of all the sub-arrays 
A=[1,2,3,4,5]
print(Subarray(A))                                         # The answer is printed here 
=======
# Subarray : Continuoes part of array 
# 1 2 3 4 5 
# {2,3}  wrong
# 2 4 1 6 -3 7 8 4 
# 1 6 8 
# 1 4 
# 6 1 4 2 
# 7 8 4 
# No of subarrays = N * ( N + 1 ) / 2 
# 
# Given an array find the sum of all subarray
# Example array = {3,2,5}
#               --> 3
#               --> 3 2 
#               --> 3 2 5 
#               --> 2 
#               --> 2 5 
#               --> 5 
# 
# Direct approach
# for each subarray, Iterate and get the sum 
# Below is the code for the above approach
def Subarray(A):
    ans=0
    for s in range(len(A)):                                # s iteration element travels all the elements in the sub array 
        for u in range(len(A)):                            # for every s, u travels along with it 
            sum=0                                          # To process the sum of the sub-array we are using sum variable to store the sum of the sub-array 
            for b in range(u+1):                           # This loop is used to iterate all the elements in the sub-array 
                sum=sum+A[b]                               # Summing the elements 
            ans=ans+sum                                    # After processing the sum of the current sub-array, we are appending the progressed sum to the next sub-array sum calculation 
    return ans                                             # Returning the overall sum to the main function 
# But the above approach time complexity is O(n^3)
# and process the sum of all the sub-arrays 
A=[1,2,3,4,5]
print(Subarray(A))                                         # The answer is printed here 
>>>>>>> efaf86c7ee90cea27ac78c43a76e224813039749
