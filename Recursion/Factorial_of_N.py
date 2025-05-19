# Problem Statement 
# Write a program to find the factorial of the given number A using recursion 
# Note : The factorial of a number N is defined as the product of the numbers from 1 to N 
# Input Format : First and only argument is an integer A 
# Output Format : Return an integer denoting the factorial of the number A 
# Input A = 4
# Output : 24         Explanation --> Factorial of 4 = 4 * 3 * 2 * 1 ==> 24 
# Below is the python code for the above problem 
def FactorialofaNumber(A):
    if A==0:                                # Base case condition A==0, reaching where A becomes 0 we are returning the calculation recall function which are stored inside the stack 
        return 1 
    else:
        return A*FactorialofaNumber(A-1)    # Until we reach the base condition the else condition will be used for calculation of the factorial of a number bycalling the function itself with minimal values 
#
#
# 5 factorial = 5 * 4 * 3 * 2 * 1  => 120
Result = FactorialofaNumber(10) 
print(Result)
