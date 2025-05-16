# Problem Statement 
# Given an integer N. Count the set bits in N
# N=12  --->   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
# Ans = 2
# The approach is using the using two functions 
# One fucntion counts the set bit by the return answer of other function
# Other one checks the i th bit is set or not; if set it returns true if don't it returns false 
# Below is the python code for the above problem statement 
#
def CheckIthBit(A,i):                 
    if(A&(1<<i))==0: return False           # Brief explanation 
    else : return True 

def CountSetBits(A,i):
    Count=0                                  # Using the Count variable to count the set bits
    for bit in range(32):                    # Running the loop from 0,32 
        if (CheckIthBit(A,bit)):             # The Value A is passed with bit in range of 0 to 32 on CheckIthBit function ; if the function returns True : count=count+1 ; else count remains same
            Count=Count+1
    return Count                             # After every process we are returning the count of set bits 
 
 
 # Brief explanation 
 # If (A&(1<<i))==0               not the bit range is 1 which is passed from the CountSetBits function
 # given number A=15                                       8 4 2 1 
 #                                                         1 1 1 1 
 # bit range = 1     if(A&(1<<1))==0: False else True ->         1      True  Count=1
 # bit range = 2     if(A&(1<<2))==0: False else True ->       1        True  Count=2
 # bit range = 3     if(A&(1<<3))==0: False else True ->     1          True  Count=3
 # bit range = 4     if(A&(1<<4))==0: False else True ->   1            True  Count=4
 