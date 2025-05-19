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
def DecFunction(A):                                # Creating a function that is used for printing 10 to 1 
    if A == 0 :
        return 1
    else : 
        print(A,end=' ')                           # Printing of the values will be done here without being get to stored in the main function 
        DecFunction(A-1)
    
def IncFunction(A):                                # Creating a function that is used for printing 1 to A
    if A == 0 : 
        return 1 
    else :
        IncFunction(A-1)
        print(A,end=' ')                            # Same here too printing of the number from 1 to A will be done here without being stored or returned to the main function 

def DecThenInc(A):                                  
    DecFunction(A)                                  # Calling the Decreasing Print Function 
    IncFunction(A)                                  # After the call of DecFunction and it's work , then IncFunction will be called 

print(DecThenInc(10))


    