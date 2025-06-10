# Square Year
# https://codeforces.com/problemset/problem/2114/A
def Problem26():
    t=int(input())                  # <-- No of test cases
    for _ in range(t):              
        a=int(input())              # <-- Input number from the user 
        a1=0
        a2=0
        for i in range(a):
            a1=a1+1
            if (a1*a1)+(a2*a2)==a:
                print(a1," ",a2)
            else:
                a2=a2+1                             # Half proper binary search 
        

Problem26()

# Approach 2 
           

def Problem26():
    t = int(input())                                # Number of test cases
    for _ in range(t):
        a = int(input())                            # The number to check
        found = False
        for a1 in range(a + 1):                     # Try all values of a1 from 0 to a          1 : 1,2,3,4,5,6
            for a2 in range(a + 1):                 # Try all values of a2 from 0 to a          
                if (a1 * a1) + (a2 * a2) == a:
                    found = True
                    break                           # Exit inner loop if found
            if found:
                break                               # Exit outer loop if found
        if found:
            print(a1,a2)
        else:
            print(-1)

Problem26()
