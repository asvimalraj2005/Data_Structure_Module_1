# Spell Check
# Problem Statement 
# Timur likes his name. As a spelling of his name, he allows any permutation of the letters of the 
# name. For example the following strings are valid spellings of his name : Timur, miurT, Trumi, mriTu. 
# Note that the correct spelling must have uppercased T and lowercased other letters
# Today he wrote string s of length n consisting only of uppercase or lowercase latin letters. He asks 
# you to check if s is the correct spelling of his name 
# Input : The first line of the input contains an integer t(1<=t<=10^3) the number of test cases 
# The first line of each test case contains an integer n(1<=n<=10) the length of string 8 
# The second line of each test case contains a string 8 consisting of only uppercase or lowercase latin characters
# Output
#For each test case, output "YES" (without quotes) if s
# satisfies the condition, and "NO" (without quotes) otherwise.
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
# 
# Below is the solution for the problem 
def solve():                                  # Here an function named solve is created with an parameter of A 
   t=int(input())                             # No of test cases 
   for _ in range(t):                         # " _ "  acts as the placeholder and runs until t times
       n=int(input())                         # string length
       s=input()                              # string input     
       if n!=5:                               # If length is not equal to 5 
           print("NO")                        # Print("NO")
           continue                           # Continuing the loop after skipping the sorted condition check 
       if sorted(s)==sorted("Timur"):
           print("YES")                       # If n==5 and satisfies the condition we are printing YES
       else:
           print("NO")                        # Else NO is printed out from the else block 

solve()

#
# https://codeforces.com/problemset/problem/1722/A
