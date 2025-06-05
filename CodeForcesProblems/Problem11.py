# Divisibility Problem
# https://codeforces.com/problemset/problem/597/A
# Find the number of K-divisible numbers on the segment [a,b]. In other words you need to find the number of such integers values x that a<=x<=b and x is divisible by k
# Input : The only line contains three space-separated integers k, a and b 
#         (1<=k<=10^18;-10^18<=a<=b<=10^18)
# Output : Print the required number 
# Example Input : 1 1 10   -> 10
#                 2 -4 4   -> 5 
# Explanation where 2 is k ; -4 is a and 4 is b 
# Values x inbetween 'a' and 'b'[inclusive though], where the x integer value should be divisible by 'k' 
# Below is the code(easy problem)
def DivisibilityProblem():
    k,a,b=map(int,input().split())
    list_ans=[]
    for x in range(a,b+1):                  # Created a for loop that iterates between a and b with the iterator x 
        if x % k == 0 :                     # if x value between a and b gives us the remainder 0 when x gets divided by k
            list_ans.append(x)              # if the x value satisfies the condition then we are appending the x value to the ans_list 
    
    print(len(list_ans))

DivisibilityProblem()