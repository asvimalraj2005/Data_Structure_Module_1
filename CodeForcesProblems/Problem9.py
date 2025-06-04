# Plus or Minus 
# You are given three integers a, b and c such that exactly one of these two equations is true:
# a + b = c
# a - b = c 
# Output + if the first equation is true, and - otherwise 
# Input : The first line contains a single integer t(1<=t<=162) the number of test cases
#         The description of each test case consists of threee integers a,b,c(1<=a,b<=9,-8<=c<=18).
#         The additional constraint on the input: It will be generated so that exactly one of the two equations will be true
# Output : For each test case, output either + or - on a new line, representing the correct equation
# Example Input : 3
#                 1 2 3      1+2=3 which equals to a+b=c
#                 3 2 1      3-2=1 which equals to a-b=c
#                 2 9 -7     2-9=-7 which equals to a-b=c
# Example Output : +    
#                  -
#                  -
# Below is the following code for the above problem statement 
def PlusorMinus():
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        if a+b==c:
            print("+")
        elif a-b==c:
            print("-")

PlusorMinus()

