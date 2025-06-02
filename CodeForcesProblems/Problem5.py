# A string is called square if it is some string written twice in a row. For example, the strings 
# "aa", "abcabc" are square. But the strings "aaaa" and "abcdabc" aren't square.
# For a given string s determine if it is square or not 
# Input :
# The first line of input data contains an integers t(1<=t<=100) the number of test cases 
# This is followed by t lines, each containing a description of one test case. The given strings
# consist only of lowercase latin letters and have lengths between 1 and 100 inclusive
# Output :
# For each test case, output on a separate line:
# YES if the string in the corresponding test case is square
# NO otherwise 
# Below is the solution for the above problem
                                     # This does require a two-pointer approach where the given string length is divided by 2 
                                     # where the first pointer is used to start from first index of the strign and the second is used to start from the middle of the string index 
                                     # first pointer moves until it reaches the half of the string index length
                                     # second pointer moves until it reaches the end of the string index length 
def CheckString():
    t=int(input())
    for _ in range(t):
        A=input()
        pointer_1=0
        pointer_2=len(A)//2
        N=len(A)
        for i in range(len(A)):
            if A[pointer_1]!=A[pointer_2]:
                print("NO")
            else:
                print("YES")
                pointer_1=pointer_1+1
                pointer_2=pointer_2+1

# The code above will not work for certain conditions due to logical indexing issue 
# Below is the correct code for the problem statement 
def CheckString():                                          
    t = int(input())                                        # T test cases 
    for _ in range(t):                                      # Iterator for T test cases 
        s = input()                                         # String variable s 
        n = len(s)                                          # String length n
        if n % 2 != 0:                                      # Odd square length is not a perfect square 
            print("NO")                                     # Prints NO
            continue                                        # Skipping the iteration process 
        half = n // 2                                       # If it is even dividing the length of the string into two equal halves 
        if s[:half] == s[half:]:                            # String slicing 
            print("YES")                                    # If it is same YES will be printed on the screen 
        else:
            print("NO")                                     # If don't NO 


https://codeforces.com/problemset/problem/1619/A




