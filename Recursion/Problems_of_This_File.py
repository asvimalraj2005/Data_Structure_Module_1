# Recursion is used for backtracking, trees, Dynamic Programming, Grpahs
# Sorting Algorithm's[Merge , Sort, Quick Sort]
# Function calling itself 
# Use --> Break down big problem into smaller subproblem and solve it using solution of subproblems 
# Steps of writing recursive code 
# Defining Function --> Decide exactly what the function will do for the given problem 
# Main Logic --> Break problem down into smaller subproblems to solve the bigger problem 
# Base Condition --> Identify the inputs for which we need to stop,
# Smallest sub-problem for which we already know the answer 
# Example problem for recursion 
# Sum of first N natural numbers; formula for this --> N(N+1)//2
# Sum ( 4 ) = 1 + 2 + 3 + 4   -->
#             _________ 
#           Sum ( 4 - 1 )  + 4 
# Sum ( N ) = Sum ( N - 1 ) + N 
# Below is code for the above problem 
def SumofRange(N):
    if (N==1):
        return 1 
    return SumofRange( N - 1 ) + N 

Result=SumofRange(10)
print(Result)