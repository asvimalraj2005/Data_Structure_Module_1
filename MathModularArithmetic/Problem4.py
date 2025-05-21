# Problem Statement 
# Given an integer array A of size N. You have to delete one element such that the 
# GCD(Greatest Common Divisor) of the remaining array is maximum 
# Find the maximum value of GCD
# Input Format : First argument is an integer array A 
# Output Format : Return an integer denoting the maximum value of GCD
#
#
# A = [ 12 , 15 , 18 ]
# O/P : 6 
# If you delete 12, gcd will be 3 
# If you delete 15, gcd will be 6 
# If you delete 18, gcd will 3 
#
#
# Maximum value of gcd is 6 
# Just use a variable which calculates the max between the current gcd and calculated gcd 
# By using max function 
# 
#
# Problem solution Approach use nested loop for every i delete the element in the array and for every j run 0 to (N-1) and within the inner loop have an variable named max_gcd calulate by using max function and store the gcd in max_gcd
def GCD(A,B):
    if B==0:
        return A
    else:
        return GCD(B,A%B)

def MaxGCDofanArrayByDeletingOnebyOne(A):               # Ain't a good code function name but it nevertheless enough 
    max_gcd=0
    N=len(A)
    
    for i in range(N):                                  # Outer Loop for every i the element is removed 
        temp=A[:i]+A[i+1:]                               # The i th element is removed here and element is stored inside the temp list so that it will not modify the original list  
        g=temp[0]                                       # Storing the first element in temp 
        for j in range(1,len(temp)):                    # For every i iteration , j will iterate from 0 to N-1 of the array 
            g=GCD(g,temp[j])                            # Calculating the GCD 
        max_gcd=max(max_gcd,g)                          # Max GCD after every element got removed and calculated 
    return max_gcd

A=[12,15,18,20,28]
print(MaxGCDofanArrayByDeletingOnebyOne(A))
