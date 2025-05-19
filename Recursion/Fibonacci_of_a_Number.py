# Find Fibonacci 
# Problem Description 
# The Fibonacci numbers are the numbers in the following integer sequence.
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144 , ....
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation <- Recurrence relation is a mathematical terms and used for the Geometric Progression and Arithmetic Progression 
# Formula for recurrence relation is Fn = Fn-1 + Fn-2
# Given a number A , find and return the Ath Fibonacci Number using recursion. Given that F0 = 0 and F1 = 1
# Input Format : First and only argument is an integer A.
# Output Format : Return an integer denoting the Ath term of the sequence 
# A = 2 
# O/P = 1 
# Explanation => F(2) = F(1) + F(0) =1 
# Below is the python code for the above problem statement 
def FibonacciofaNumber(A):
    if A <= 1 :                                                                     # Base Case Condition
        return A 
    else :
        return FibonacciofaNumber ( A - 1 ) + FibonacciofaNumber ( A - 2)           # Formula used for calculation of Nth Fibonacci Number 

A = 5
Result = FibonacciofaNumber ( A )
print(Result)

