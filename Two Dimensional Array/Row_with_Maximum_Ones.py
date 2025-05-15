# The problem statement says we should return the row index which has a lot of ones in simple terms 
# Brute force method is using two loops, the outer loop iterates over the rows and the inner loop iterates over the column elements 
# When we are iterating over the rows and columns we should have to use two counting variable, the first counting counter variable counts the total no of ones (1's) in the row while the other updates with itself by finding the max of the second counter and first counter 
# This shows which row has the maximum ones 
# Constraints -> If two rows have the maximum number of 1 then return hte row which has a lower index 
# Expected time complexity is o(rows+columns)
# Example for the above passage 
# [  [0, 1, 1],        Counter_1=2      Counter_2=Max(Counter_1,Counter_2)                  Simple another way whatever the rows has the following maximum ones' which is equal to the previous value just store the current index of the row in the list and return the min index 
#    [0, 0, 1],        Counter_1=1      Counter_2=Max(Counter_1,Counter_2)
#    [0, 1, 1]  ]      Counter_1=2      Counter_2=Max(Counter_1,Counter_2)
# Below is the simple following python code 
# O(n^2) Complexity 
def Row_with_Maximum_Ones(Mat):
    
    counter_two=0
    ans_list=[]
    
    N=len(Mat)
    for i in range(len(Mat)):
        counter_one=0
        for j in range(len(Mat)):
            if Mat[i][j]==1:
                counter_one=counter_one+1
        counter_two=max(counter_one,counter_two)
        if counter_one==counter_two:
            ans_list.append(i)
    
    if len(ans_list)>1:     # If there are multiple rows with the maximum number of 1's, find the second smallest 
        ans_list.sort()     # Sort the rows to find the smallest two
        return ans_list[1]  # Return the second smallest row index 
    else:
        return ans_list[0]  # Return the only row with maximum 1's if only one row is present 

Mat=[[1,1,1,1,1],[1,1,1,1,1],[0,1,1,0,1],[1,1,1,1,1]]  # Row 1 , row 2 , row 3 
print(Row_with_Maximum_Ones(Mat))
    