# You are given two positive integers a and b. In one move you can increase a by 1 ( replace a with a + 1 ). 
# Your task is to find the minimum number of moves you need to do in order to make a divisible by b. It 
# is possible, that you have to make 0 moves, as a is already divisible by b. You have to answer t independent
# test cases 
# Input : The first line of the input contains one integer t(1<=t<=10^4) the number of test cases. Then t test cases follow
#         The only line of the test case contains two integers a and b (1<=a, b<=10^9)
# Output : For each test case print the answer - the minimum number of moves you need to do in order to make a divisible by b 
# Example Input : 5
#                 10  4 
#                 13  9
#                 100 13
#                 123 456
#                 92  46 
# Example Output : 2
#                  5
#                  4
#                  333
#                  0 
# Problem solving approach for the above problem
# we should make a that is divisible by b by incrementing a by 1 
# 10 , 4   a is 10 and b is 4 where 10 is not divisible by 4 and gives us the remainder 2, so we increment 10 to 12 thus the count of increment becomes 2 and 12 % 4 == 0 
# 13 , 9   a is 13 and b is 9 where 13 is not divisible by 9 and gives us the remainder 4 , so to perfectly divide a by b with remainder as 0 , we increment a by 5 times so thus the number becomes as 18, now 18%9==0 
# so on and so forth 
# Below is the python code for the above problem statement 
def DivisibilityProblem():
    t=int(input())
    for _ in range(t):
        a=int(input())
        b=int(input())                        # <-- a , b input lines can be converted into ' a,b = map(int(input().split())) '
        count=0                               # Incrementing by one is counted by the count variable 
        while(a%b!=0):                        # until a is perfectly divides by b we are incrementing the value of a 
            a=a+1                           
            count=count+1                     
        print(count)                          # Printing the count 
        

# https://codeforces.com/problemset/problem/1328/A

