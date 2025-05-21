# Given N array elements. Find the count of pairs ( i , j ) such that ( arr[i] + arr[j] ) % m = 0
# The index element when traversed in the array where i=0 and j=i+1, it will check if any pairs does gives the remainded as 0 then count the pairs and return it
# Note : i ! = j and pair ( i , j ) is same as pair ( j , i )
#
#
# arr -> [ 4 , 7 , 6 , 5 , 8 , 3 ]     M = 6 
# Pairs that satisfy ( arr [i] + arr [j] ) % 6 == 0 are : 
# ( 4 + 8 ) % 6 = 0          Count = Count + 1    -> 0
# ( 3 + 3 ) % 6 = 0          Count = Count + 1    -> 1
# ( 7 + 5 ) % 6 = 0          Count = Count + 1    -> 2 
#
#
# arr 2 -> [ 1 , 2 , 3 , 4 ]    M = 5
# Pairs that satisfy ( arr [i] + arr [j] ) % 6 == 0 are :
# ( 2 + 5 ) % 7 = 0          Count = Count + 1    -> 0
# ( 5 + 2 ) % 7 = 0          Count = Count + 1    -> 1
# ( 3 + 4 ) % 7 = 0          Count = Count + 1    -> 2
#
#
# Approach 1 use a nested for loop; the outer for loop will iterate over 0 th index to len(Array)-1 range but the inner loop will traverse for every ith index it will traverse every element in the array 
# Thus makes the approach one is O(n^2) and not efficient 
# Below is the python code for the approach 1
#
def PairSumCountNestedLoop(A,M):
    N=len(A)
    Count=0
    for i in range(N):                              # Outer Loop i for every i 
        for j in range(i+1,N):                      # j will run i+1 to N-1 
            if (A[i]+A[j])%M==0:                    # Using the formula to check whether the element i,j produces the remainded as 0 
                Count=Count+1                       # If does Count will get incremented by one 
    return Count                                    # Returning the count 

A=[1,2,3,4]
M=5
print(PairSumCountNestedLoop(A,M))
#
#
# For the above approach this formula is used (A[i]+A[j])%m=0
# => ( A [i] % m ) + ( A[j] % m ) % m =0
#     |---------------------------------------> ( m - 1 ) +
#                    |----------------------------------->  ( m - 1 ) = 2 m - 2 
#
# 0 , m , 2 m , 3 m 
# Find pairs such that sum is 0 or m 
# 
#
# Approach two for all element i , count of elements on left / right that form a pair with sum 0 or m. 
# Below is the python code
#
def PairSum2(A,M):
    ans=0
    F=[0]*M
    for i in range(len(A)):
        x=A[i]%M                            # This computes the remainder of each element    
        if x==0:                            # If the remainder of A[i] is zero which is stored in variable x , then it can be paired only with other numbers that also give remainder 0 to satisft ( A + B ) % M = 0 
            ans=ans+F[0]                    # So you add the number of elements you have already seen with remainder o from the frequency array 
        else:                               # For all other remainders x, you need a number with remainder M-x so that ( x + M - x ) % M = M % M = 0
            ans=ans+F[M-x]
        F[x]=F[x]+1                         # For every valid pairs, you have now seen one more element with remainder x 
    
    return ans                              # Returning the answer
#
#
A1=[1,2,3,4,5,6,7]
M=5
print(PairSum2(A1,M))
