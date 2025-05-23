
# Problem Statement 
# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output
# Note : A linear time complexity is expected and you should avoid use of any library function.
# Input Format --> First Argument is a 1-D array representing A
#                  Second Argument is also a 1-D array representing B
# Output Format --> Return a 1-D vector which you got after merging A and B 
#                   
# Input A = [ 4 , 7 , 9 ]
#       B = [ 2 , 11 , 19 ]
# Output -> [ 2 , 4 , 7 , 9 , 11 , 19 ]
# 
# Problem solving approach use two pointers over a while loop and each one of the while loop is associated with the array A and array B 
#   i
# [ 4 , 7 , 9 ]     i < j <-->   4 < 2    2 is less than 4 so we are going to add 2 in the empty array
#   j              
# [ 2 , 11 , 19]                after the adding the minimum element we are incrementing the minimum element found array index pointer now j will be moved to the next index 
#
# empty_array = []  --> [ 2 ]
#
#   i
# [ 4 , 7 , 9 ]     i < j <-->  4 < 11    4 is less than 11 so we are going to add 4 in the empty array 
#       j              
# [ 2 , 11 , 19]                after the adding the minimum element we are incrementing the minimum element found arrat index pointer now i will be incremented to the next index 
#
# empty_array = []  --> [ 2 , 4 ]  
#
#       i
# [ 4 , 7 , 9 ]     i < j <--> 4 < 11     7 is less than 11 so we are going to add 7 in the empty_array 
#       j                       
# [ 2 , 11 , 19]                incrementing the i by 1 and i pointer variable will be now pointing towards the next index 
#
# empty_array = []  --> [ 2 , 4 , 7 ]  
#
#           i
# [ 4 , 7 , 9 ]     i < j <--> 9 < 11    9 is less than 11 so we are going to add 9 in the empty array 
#       j              
# [ 2 , 11 , 19]                 incrementing the i by 1 and we have reached the end here so now we should add the array elements of B in empty_array
#
# empty_array = []  --> [ 2 , 4 , 7 , 9 ]  
#
#
# For this we should have to use another two while loops to ensure that we don't leave any elements in the array A and B 
#
# Below is the python code for the above approach
#
def MergeSorted(A,B):
    
    empty_list = []                                 # Empty list is used here for the result 
    y2 = 0                                          # Pointer 1 
    y1 = 0                                          # Pointer 2 
    while y2 < len(A) and y1 < len(B):              # y2 and y1 will be incremented until it reaches the length of both the array 
        if A[y2] < B[y1]:                           # Comparison between the A[y2] index 0 element of A and B[y1] index o element of B 
            empty_list.append(A[y2])                # If A array element is leeser then we append it to the array 
            y2 += 1                                 # Incrementing the pointer 
        else:
            empty_list.append(B[y1])                # Else if the B element is greater than the A element we are appending to the pointer 
            y1 += 1                                 # Incrementing the B array element pointer 

    while y2 < len(A):                              # Adding the non-calculated element from the array A to the empty_list through by using pointers 
        empty_list.append(A[y2])                    # Appending the element to the empty_list 
        y2 += 1                                     # Incrementing the pointer 

    while y1 < len(B):                              # Adding the non-calculated element from the array A to the empty_list through by using pointers 
        empty_list.append(B[y1])                    # Appending the element to the empty_list 
        y1 += 1                                     # Incrementing the pointer 

    return empty_list                               # Returning the empty_list nope the name may convey different meaning here but it has the values of the array A and array B in sorted manner 

    
A=[1,2,3,4,5]
B=[1,2,3,4,5]
print(MergeSorted(A,B))
