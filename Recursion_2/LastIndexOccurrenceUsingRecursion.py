# Problem Statement 
# You are given an array A of size N. Write a recursive function that returns the last index at
# which an integer B is found in the array 
# Note : If B is not found anywhere in the array then return -1 
# Input Format : The function contains two arguments 
#                The first argument is the array A 
#                The second argument is the element B that is to be searched 
# Output Format : Return the last index of B from the list in integer fromat if B is present in the array, else return -1 
# Input : A = [ 6 , 5 , 6 , 2 ]
# B = 6 
# Explanation : At index 0 we have 6 which is equal to B, but it's not the last occurence
#               At index 1 we have 5 
#               At index 2 we have 6 which is equal to B, and it's the last occurence as well 
# So the output is 2 and not 0 
# Moving onto the problem solving approach 
# We are gonna use an helper function inside the Main function where the function iterates over the array using an index variable pointer where every index variable pointer increments by 1 for every recursive call 
# And the main if condition comes here which plays the good part in finding the last occurence just use if A[index]==B and A[index+1]!=B so by using AND we can say that both the index current element and index next element will get checked if does satisfies the condtion we can simply return current value index if not return -1 
# Below is the python code for the above approach 
def LastOccurence(A,B):                                             # Function named LastOccurence with two parameters A array and B element 
    def Helper(Index):                                              # Helper function is used to iterate over the array elements by using Index variable pointer will be get incremented by 1 for every recursive calls 
        if Index==len(A):                                           # Base case if the Index variable reaches the end the array index then return None because the previously travelled array elements is not equal to B 
            return None 
        elif A[Index]==B and A[Index+1]!=B or Index==len(A)-1:      # A[Index]==B and A[Index+1] where the current index and the next index value should be equal if we are in len(A)-1 in range if we reach the last index where the array looks like this A = [ 6 , 6 , 6 , 6 , 6 , 6 , 6 ] then Index=len(A)-1 will be used here and we return the last array element index 
            return Index
        return Helper(Index+1)                                      # Recursive Calling  
    return Helper(0)                                                # Recursive Calling 

A=[1,2,3,4,5,6,6,6,6,7]
B=6
print(LastOccurence(A,B))

            