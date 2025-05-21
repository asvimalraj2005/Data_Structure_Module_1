# Problem Statement 
# Given an array of integers A. Calculate the sum of A[i]%A[j] for all possible i,j pairs,
# Return sum % ( 10 ^ 9 + 7 ) as an output 
# Input Format : The only argument given is the integer array A
# Output Format : Returns a single integer denoting sum % ( 10 ^ 9 + 7 )
# Approach 1 just use nested for loop and iterate over the values in the array and use an sum variable for calculating the entire GCD sum of the array with pairs of i+j
# Below is the python code for the above problem statement 
def TotalSumModulo(A):
    MOD = 10**9 + 7                                                     
    Entire_Sum = 0                                          # Variable used to store the entire sum of the modulus operation which have been done in the iteration
    for i in range(len(A)):     
        for j in range(len(A)):
            Entire_Sum = (Entire_Sum + A[i] % A[j]) % MOD   # After calculating the modulus of A[i] and A[j] value which gives the remainder and then we are limiting the running Entire_Sum value by using MOD variable value 
    return Entire_Sum                                       # Returning the Entire Sum 


A=[1,2,3,4,5,6]
print(TotalSumModulo(A))

        