# Odd one out 
# A,B,C any one of them will be equal, find the unique one 
# Input : t is the number of test cases 
#         only line a,b,c 
# Below is the code 
def Problem15():
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        if a^b==0:
            print(c)
        elif b^c==0:
            print(a)
        elif a^c==0:
            print(b)
Problem15()