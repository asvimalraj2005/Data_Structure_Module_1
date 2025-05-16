# Problem statement
# A group of computer scientists is working on a project that involves encoding binary numbers.
# They need to create a binary number with a specific pattern for their project. The pattern requires
# A 0's followed by B 1's followed by C 0's. To simplify the process, they need a function that takes 
# A, B and C as inputs and returns the decimal value of the resulting binary number. Can you help them by writing a function that can solve this problem efficiently 
#
#    ---- 0's ----     ---- 1's ----    ---- 0's ----         -> Decimal no ( Conversion is the answer )
#         A                 B                C
# 
# Example :  A = 4 , B = 3 , C = 2 
#            0 0 0 0  1 1 1  0 0     -> 28   ( Ans = 28 ) not though 8 4 2 1                          1 <= A , B , C <= 20 
#                     ↑ ->  2 1 2 
#                     2 + 3 -1 = 4  
#                     C + B -1 = Times of A bit iterated for the upcoming ones 
#
# Below is python code       

def ScientistProblem(A,B,C):        # Passing A , B , C as the parameters for the ScientistProblem
    ans=0                           # Initialising the ans variable to create the number with the bits fount in the position 
    for i in range(C,B+C):          # Running the loop from C to B+C         
        ans |= (1<<i)           # Creation of number through the bits is done here
    return ans                      # Returning the answer


A=4
B=5
C=1
print(ScientistProblem(A,B,C))
    
