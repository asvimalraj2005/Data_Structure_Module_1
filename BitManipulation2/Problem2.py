# Problem Statement 
# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice 
# Find the two integers that appear only once 
# Note : Return the two numbers in ascending order 
# Input Integer : The first argument is an array of integers of size N 
# Output Format : Return an array of two integer that appear only once 
# Same approach 1 from the problem1.py in the Bit Manipulation 2 Folder 
# By using the XOR operator we are easily find the first unique and second unique number inside the given List A 
# Solution Approach 
# Approach method 1 by using Count function 
# Iterate over the list and check the element of the list by using the count function and validate it with other element variable with predefined variblw with value one
# Create an empty list and append the value which satisfies the condition, and use set to append the counted values from the List A
# Below is the python code for the Approach one 
def FindTwoUniqueOverCommonTwice(A):
    Ans_List=[]                                             # Ans_List is used to store the unique elements from the List A
    Seen = set()                                            # The counted List A elements will get stored in here for not to get counted in the further same elements as present inside the set 
    for element in A:                                       # Traversing the List A by using the iterator named element and accessing every element in A 
        if element not in Seen:                             # If the A th element is not present in the Seen named set we are moving to the next if condition 
            if A.count(element) == 1:                       # By using the count function we are checking A th element how many times present inside the list A if it is satisfies the condition which is the count equals to 1 
                Ans_List.append(element)                    # Then we are appending the Element which has count one to Ans_List 
            Seen.add(element)                               # Atlast we are adding the counted element in the set seen for in the future iteration to not get counted which are present inside the list A 
    return Ans_List                                         # Returning the Ans_List 

# A ^ A = 0 
# A ^ B != 0        <--- will have one set bit, whic is set in either A or B but not both 
# A != B 
# Example [ 1 , 1 , 2 , 2 , 5 , 7 , 7 , 6 , 8 , 8 ]
# Now 5 --> 0 1 0 1 
# Now 6 --> 0 1 1 0 
# 5 ^ 6 --> 0 0 1 1  --> 3    Use this bit and divide the array into 2 parts 
#                             1 ) All elements with this bit 1
#                             2 ) All elements with this bit 0 
# 1 position of bit which is set in the particular in answer 1 and unset in the answer 2 
# For a particular position we are going to check the bit is set or not
# In first part answer 1 will be present 
# In second part answer 2 will be present 
# Elaborate explanation
# arr -->  10    8    8    9    12    9    6    11    10    6    12    17 
#          1010  1000 1000 1001 1100  1001 0110 1011  1010  0110 1100  10001   
#
# Indexes                               4  3  2  1  0
# XOR of all elements --> 11 ^ 17       0  1  0  1  1
#                                  ^    1  0  0  0  1
#                                       1  1  0  1  0  -> 26   
# Rightmost set bit                              | 
# Position of set bit          =                 1 
#
# Next step                                                                                        |    <-- 
# List elements which has set bit in the position index 1 are considered as set : example 10 : 1 0 1 0        then 10 will be considered as set 
#                                                                                 example 6  : 0 1 1 0        then 6 will be considered as set 
#
# Set bit elements are :  10  ,  6  ,  11  , 10  , 6                    Now XOR of all the elements is 11
# Unset bit elements are :  8  ,  8  ,  9  ,  12  ,  9  ,  12  , 17     Now XOR of all the elements is 17 
# Below is the python code 
def FindUniqueTwoAmongCommonTwice(A):
    
    # Finding the XOR of all the elements 
    XORFIRSTELEMENT=0
    for i in range(len(A)):
        XORFIRSTELEMENT = XORFIRSTELEMENT ^ A[i]
    
    # Find any set bit position in XOR 
    position = -1 
    for b in range(32):
        if (XORFIRSTELEMENT & (1<<b)) > 0 : 
            position = b
            break
    
    # Split the array on the basis of position bit 
    
    Ans_1=0
    Ans_2=0
    N=len(A)
    for i in range(N):
        if ((A[i]&(1<<position))>0):
            Ans_1^=A[i]
        else : 
            Ans_2^=A[i]
    
    return Ans_1,Ans_2


A=[1,1,2,3,3,4,5,5,7,7]
Result1,Result2=FindUniqueTwoAmongCommonTwice(A)
print(Result1," ",Result2)
    


        


