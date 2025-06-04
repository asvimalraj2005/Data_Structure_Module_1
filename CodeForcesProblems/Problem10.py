# Problem Statement
# You are given three integers a,b and c. Determine if one of them is the sum of the other two
# Input : The first line contains a single integer t(1<=t<=9261)- the number of test cases 
#         The description of each test case consists of three integers a,b,c,(0<=a,b,c<=20)
# Output : For each test casem output "YES" if one of the numbers is the sum of the other two, and "NO" otherwise
#          You can output the answer in any case(for example, the string "yEs","yes","Yes" and "YES" will be recognized as a positive answer 
# Below is the approach on how to solve the above problem 
# By using three variables, list mapping, and splitting function we are getting the input and assigning to the variables 
# t is the no of test cases for how many a,b,c are got as the input from the system
# just by using simple if elif conditional statement we can easily solve the problem
# Below is the python code for the above problem
def Problem():
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        if a+b==c:
            print("Yes")
        elif c+a==b:
            print("Yes")
        elif c+b==a:
            print("Yes")
        else:
            print("No")
