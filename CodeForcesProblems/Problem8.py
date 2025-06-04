# Problem Statement 
# In search of an easy problem
# when preparing a tournament, Codeforces coordinates try their best to make the first problem
# as easy as possible. This time the coordinator had chosen some problem and asked n people about 
# their opinions. Each person answered whether this problem is easy or hard.
# If at least one of these n people has answered that the problem is hard, the coordinator decides 
# to change the problem. For the given responses, check if the problem is easy enough
# Input : The first line contains a single integer n(1<=n<=100) the number of people who were asked to
# give their opinions. The second line contains n integers, each integer is either 0 or 1. If i-th integer is 0,
# then i-th person thinks that the problem is easy; if it is 1, then i-th person thinks that the problem is hard.
# Output : Print one word "EASY" if the problem is easy according to all responses, or "HARD" if there is at least one 
# person who thinks the problem is hard
# You may print every letter in any register "EASY","easy","EaSY" and "eAsY" all will be processed correctly 
# Example Input : 3 
#                 0 0 1 
#            O/P: HARD              <-- Reason for hard because 1 is present 
# Example Input  : 1
#                  0
#            O/P: EASY              <-- Reasin for easy because there is no 1 which represents hard
# Problem Approach
# Below is the problem solution code which comprises correctly to the above problem statement 
def problem():      
    n = int(input())                                    # <-- This n input represents no of users 
    opinions = list(map(int, input().split()))          # <-- By using list and map function we are getting multiple numbers as input , splitting them and storing into list named opinions 
    if 1 in opinions:                                   # <-- If any 1 found in the opinions list then the answer will be HARD
        print("HARD")   
    else:   
        print("EASY")                                   # <-- If not one is not found in the opinions list then the answer will be EASY 

problem()                                               # <-- Calling the function to get executed 
    

# https://codeforces.com/problemset/problem/1030/A