# Problem Statement 
# Given arr[]. Calculate GCD of entire array 
# Problem solution approach 
# Iterate over the array and use the GCD function seperately and pass the iterated values to the GCD function and return the calculated value to the for loop iteration for further calculation 
# Below is the python code for the above approach 

# Function to calculate the GCD 
def GCD(A,B):
    if B==0:
        return A
    else: 
        return GCD(B,A%B)                           # For every iteration happens in the EntireGCD array element this function is used and return the value to g element 
def EntireGCD(A):
    g=A[0]
    for i in range(len(A)):
        g=GCD(g,A[i])
    
    return g                                        # Total GCD of the array is calculated and returned 

A=[1,2,3,4,5,6,7]                                   # I think the GCD is 2 
print(EntireGCD(A))