# Problem Statement
# Decreasing Increasing in one function 
# Print N numbers in decreasing order and then in increasing order 
# You are given a positive number N
# You are required to print the numbers from N to 1 
# You are required to not use any loops. Don't change the signature of the function DecThenInc function
# Note : Please print an new line after printing the output 
# Input Format : The first line contains a single integer N
# Output Format : A single line having number printed from N to 1 and then from 1 to N 
# Below is the python code
def DecFunction(A):
    if A == 0 :
        return 1
    else : 
        print(A,end=' ')
        DecFunction(A-1)
    
def IncFunction(A):
    if A == 0 : 
        return 1 
    else :
        IncFunction(A-1)
        print(A,end=' ')

def DecThenInc(A):
    DecFunction(A)
    IncFunction(A)

print(DecThenInc(10))


    