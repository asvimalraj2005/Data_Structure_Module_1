# Problem Statement 
# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array
# Note : Each element in the result should appear as many times as it appears in both array   
# The result can be in any order
# Input Format : First argument is an integer array A of size N
#                Second argument is an integer array B of size M
# Output Format : Return an integer array denoting the common elements
# Example Input : A = [ 1 , 2 , 2 , 1 ] 
#                 B = [ 2 , 3 , 1 , 2 ]
# Example Output : [ 1 , 2 , 2 ]
# Approach One : just use dictionary set for removing the duplicate elements in both of the array 
#                create a dictionary named Array_1=set(A) and pass A array into it 
#                create a dictionary named Array_2=set(B) and pass B array into it 
# now the Array_1 and Array_2 will be consisting of Array A values and Array B values 
# Iterate over Array_1 check whether the Array_1 element is present inside the Array_2 are not if present in the Array_2 then append to the ans_list 
# Create an ans_list for storing of an element which is present in both of the array 
# Below is the program for the above approach

# This code does not follow the rules of Each element in the result should appear as many times as it appears in both arrays.
def SameElements(A,B):
    Array_1=set(A)              # <-- Through this process we are removing the duplicate elements 
    Array_2=set(B)              # <-- Through this process we are removing the duplicate elements 
    ans_list=[]
    for element in Array_1:
        if element in Array_2:
            ans_list.append(element)
    return ans_list

A=[1,2,2,1]
B=[2,3,1,2]
print(SameElements(A,B)) 
    