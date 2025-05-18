# Problem Statement 
# Find the nth Magic Number 
# Given an integer A. Find and return the A^th magic number 
# A magic number is defined that can be expresses as a power of 5 or a sum of unique powers of 5 
# First few magic numbers are 5,25,30(5+25),125,130(125+5)
# Input Format : The onlt argument given it's integer A
# Output Format L Return the Ath magic number 
# Input Number A=3 output : 30    -->    5 25 30 125 130 625 630 ....
# Below is the python code for the above problem yet simple observation 5, 5^5, 5^5+5, 125^5, 125+5,
def NthMagicNumber(A):
    result=0                                # Result variable is initialised for the storing purpose of the answer value 
    for i in range(32):                     # Running a loop from 1 to 32 bits exclusively
        if A&(1<<i):                        # Checking if A&(1<<i) i.e checking the ith bit is set or not; if ith bit set we are moving down to the condition  
            result=result+5**(i+1)          # After the process of checking whether the ith of A is set or not we raising the power of 5 to i and adding them to the result 
    return result                           # Returning the result 

Result=NthMagicNumber(10)                   # Explanation loop with the iterator i with run from 1 to 32  
                                            # Indexes LSB to MSB(Reverse)  6   5   4   3  2  1  0 
                                            # Indexes LSB to MSB           0   1   2   3  4  5  6       
                                            # Bit range representation     64  32  16  8  4  2  1  
                                            # A=10(Binary Representation)  0   0   0   1  0  1  0 
print(Result)                               # i=0  --> 10&(1<<i)                                .           (None = . )  and (Set = | )                    
                                            # i=1  --> 10&(1<<i)                             |
                                            # i=2  --> 10&(1<<i)                          .     
                                            # i=3  --> 10&(1<<i)                       | 
