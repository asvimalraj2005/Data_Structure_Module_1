# Problem Description 
# Print 1 to A 
# You are given an integer A, print 1 to A using using recursion
# Note : After printing all the numbers from 1 to A, print a new line 
# Input Format : First argument A is an integer 
# Output Format : Print A space-separated integers 1 to A. Note There should be exactly one space after each integer. After printing all the intergers, print a new line  
# A = 10 
# 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 
# Explanation : Print 1 to 10 space separated integers
# Below is the python recursion code for printing 1 to A without using loops 
def Print_1_to_A(A):    
    if A==0:                            # Base case condition for getting exited out from the stack recalling function 
        return 1        
    else:
        Print_1_to_A(A-1)               # The Print_1_to_A will be recalled again and again, after got recalled the new calculated value will be stored inside the stack, when A reaches the condition of A == 0 then the top value of the stack to the end value of the stack will be printed 
        print(A,end=' ')                # Stack stored values will get printed here with spacings between the values 

Print_1_to_A(10)                        # Passing the value to the function 
