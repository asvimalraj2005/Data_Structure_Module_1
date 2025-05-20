
# Prolem Statement
# Print A to 1 function
# You are given an integer A ,print A to 1 using recursion 
# Input Format : First argument A is an iteger 
# Output Format : Print A space-separated integer A to 1. Note : There should be excatly one space after each integer . Print a new line after printing the A integers 
# Input A : 10
# Output : 10 9 8 7 6 5 4 3 2 1 
# Below is the python code for the above approach 
def Print_A_to_1(A):
    if A == 0 :                     # Base case condition we stop the function recall when A is going to be zero
        return 1
    else:
        print(A)                    # Printing straight A value 
        Print_A_to_1( A - 1 )       # Decreasing the A value by one and passing the A value to the Print_A_to_1 function itself and so on 

Print_A_to_1(10)

