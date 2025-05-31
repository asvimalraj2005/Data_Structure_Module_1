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
def TensDigits(A):                             # My approach 
    A.sort()                                   # Sorting the array 
    A.reverse()                                # Reversing the array     
    min_val=min(A)                             # Finding the minimum value in the array 
    min_index=A.index(min_val)                 # Finding the minimum value's index in the array 
    A.pop(min_index)                           # Removing the element by using pop method 
    A.insert(0,min_val)                        # Insering the element at the index 0
    return A                                   # Returning the array 

A=[15,11,7,19]
print(TensDigits(A))


# Method 2 
from functools import cmp_to_key              # Importing a module named cmp_to_key from the functools library 

def compare(x,y):                              # passing value x and value y to the compare function
    tens_x=(x//10)%10                          # Dividing the value by 10 and storing the last digit by using % operator 
    tens_y=(x//10)%10
    if tens_x!=tens_y:                         # If not same 
        return tens_x-tens_y                   # returning the tens_x - tens_y
    else:   
        return y-x                             # if same returning the y-x

def tens_digit_sort_cmp(A):                    # Main function 
    return sorted(A,key=cmp_to_key(compare))   # Returning the sorted compared array to the main function


A=[10,20,32,5,63,56]
print(tens_digit_sort_cmp(A))
       
    
