# An elephant decided to visit his friend. It turned out that the elephant's house is located ar point 0 
# and his friend's house is located at point x(x>0) of the coordinate line. In one step the elephant can move 
# 1,2,3,4, or  5 positions forward. Determine what is the minimum number of steps he need to make in order to 
# get to his friend's house 
# Input the first line of the input contains an integer x(1<=x<=1000000)- The coordinate of the friend's house 
# Output Print the minimum number of steps that elephant needs to get point 0 to point x 
#
# The below will work only for the input between 1-15 
def MinimumSteps(A):                     # MinimumSteps function  
    Steps=[1,2,3,4,5]                    # List named Steps contains values of distance that the elephant can move 
    Steps_sum=0                          # Steps_sum forwards the value by calculating the Steps value until it reaches A 
    Count=0                              # Count is used to sum the total no of steps that is required by the elephant to reach friend location from 0 
    for i in range(len(Steps)):          # Iterating over the Steps list 
        Steps_sum=Steps_sum+Steps[i]     # Summing up the Steps values 
        if Steps_sum<=A:                 # If Steps_sum reaches until A 
            Count=Count+1                # Incrementing the Count 
    return Count                         # Returning the Count 

def MinimumSteps(A):
    return (A+4)//5                      # <-- Equivalent of writing to ceil(A/5)      This code works greater than 15 


# https://codeforces.com/problemset/problem/617/A
