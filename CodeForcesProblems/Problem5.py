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
def CheckSquare(A):
    str_one=str(A+A)
    print(str_one)

CheckSquare("One")