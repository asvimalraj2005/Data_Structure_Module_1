# Problem Statement
# Tens Digit Sorting 
# Givan an array A of N integers. Sort the array in increasing order of the value at the tens place
# digit of every number 
# If a number has no tens digits, we can assume value to be 0
# If 2 numbers have same tens digit, in that case number with max value will come first 
# Solution should be based on comparator 
# Input Format : A = [15,11,7,19]
# Output Format : [7,19,15,11]
# The sorted order is 7,19,15,11. The tens digit of 7 is zero, and that of 19,15, and 11 is 1 
# Method 1 by using sort() we can sort the array 
# after sorting we should reverse the array by reverse method 
# Find the minimum value from the array and store in an separate variable 
# After storing, remove the element from the modified array,
# add the stored element in the 0'th index of the modified array 
# 
def TensDigits(A):
    A.sort()
    A.reverse()
    min_val=min(A)
    min_index=A.index(min_val)
    A.pop(min_index)
    A.insert(0,min_val)
    return A 

A=[15,11,7,19]
print(TensDigits(A))
       
    