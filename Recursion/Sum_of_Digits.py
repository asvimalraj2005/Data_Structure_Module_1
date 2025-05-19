# Problem Statement 
# Given a number A, we need to find the sum of it's digits using recursion
# Input format : The first and only argument is an integer A 
# Output format : Return an integer denoting the sum of digits of the number A 
# A = 46 
# O/P = 10 
# Sum of digits => 4 + 6 => 10 
# Below is the python code for the above problem statement
def Sum_of_Digits(A):
    Total_Sum=0
    if A == 0 : 
        return 1
    else:
        Last_Digit=A%10                                 # Getting the last digit from the A 
        Total_Sum=Last_Digit+Total_Sum(A//10)           # using the Total_Sum variable for summing up the digits in A , again calling the Sum_of_Digits with removing the last digit
        
        return Total_Sum                                # After calculation we are returning the total sum calculated to the main function 
    

        