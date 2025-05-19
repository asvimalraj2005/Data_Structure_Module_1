# Problem Description 
# Print 1 to A 
# You are given an integer A, print 1 to A using using recursion
# Note : After printing all the numbers from 1 to A, print a new line 
# Input Format : First argument A is an integer 
# Output Format : Print A space-separated integers 1 to A. Note There should be exactly one psace after each integer. After printing all the intergers, print a new line 
# A = 10 
# 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 
# Explanation : Print 1 to 10 space separated integers
# Below is the python recursion code for printing 1 to A without using loops 
def Print_1_to_A(A):
    if A==0:
        return 1 
    else:
        Print_1_to_A(A-1)
        print(A,end=' ')    

Print_1_to_A(10)