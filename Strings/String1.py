# Problem Description
# You are given a character string A having length N, Consisting of only lowercase and uppercase latin letters 
# You have to toggle case of each character of string A. For example 'A' is changed to 'a', 'e' is changed to 'E' etc
# Input Format : First and only argument is a character string A 
# Output Format : Return a character string 
# Example explanation  Input  : "Hello"
#                      Output : "hELLO"
# 
# Below is the program code to change the lower case alphabets to upper case alphabets 
# and uppercase alphabets to lower case alphabets 
# 
def Solve(A):
    N=A.len()
    for i in range(N):
        if A[i]>='A' and A[i]<='Z':
            A[i]=A[i]+32
        else:
            A[i]=A[i]-32
    return A 
A="Vimal Raj"
print(Solve(A))