# Given Mat M find all the sub matrices sums 
# [ [ 4 , 9 , 6 ], 
#   [ 5 ,-1 , 2 ] ]
# [4] -> 4 , [ 4, 9] -> 13 , [ 4 , 9 , 6 ] -> 19 , [ 9 ] -> 9 , [ 9 , 6 ] -> 15 , [ 5 ] -> 5 , [ 5 , -1 ] -> 4 , [ 5 , -1 , 2] -> 6 
# [5] -> 5 , [ -1 ] -> -1 , [ 2 ] -> 2  , [ -1 ,2 ] -> 1 

# [ [4]                 [ [4 , 9 ]               [ [4 , 9 , 6 ] ]             [  [ 9 ]             [ [ 9 , 6 ] ]                [ [ 6 ]
#   [5] ]  -> 9           [5 ,-1 ] ] -> 17         [5 , -1, 2 ] ] -> 25          [ -1]  ] -> 8       [ -1 ,2 ] ] -> 16            [ 2 ] ] -> 8 

# To perform the sum of the all the sub matrices which are present inside the matrix we are going use a sub matrices summing formula 
# Result = ∑ contibution of A[i][j]
# The summation involves for all i , j 
# A[i][j] * (No of sub matrices A[i][j] is part of)
# Unnecessary things -> In how many sub-matrices do the (2,2) will be present ?
# Let's a matrix     0     1    2    3 
#                   ___________________
#                 0 |____|____|___|____|          Top left -> r -> [0,2]
#                 2 |____|____|_x_|____|                      c -> [0,2]
#                 3 |____|____|___|____|          Bottom Right -> r -> [2,4]
#                 4 |____|____|___|____|                          c -> [2,3]


# Below is where the contribution technique is used for calculating the sub-matrices of the given mat
# Loop indexes (i,j)

# Top left -> [ 0 , i ]  -> i+1   ---  (+)  = (i+1)*(j+1)       --->     (+)    =  (i+1)*(j+1)*(N-i)*(M-j)          <-- This is the used to calculate the sub matrix 
#             [ 0 , j ]  -> j+1   ---  (+)  =

# Bottom right -> [ i , N-1 ] -> N-i  ---- (+) = (N-i)*(M-j)    --->     (+)    =
#                 [ j , M-1 ] -> M-j  ---- (+) = 


# Here comes the explanation the top left is used to calculate the total no of sub matrices in which index (2,2) element is present 
# The bottom right is used to calculate the how many sub matrices do the element (2,2) contained init. 
# 2,2 will present in 2,2 ; 2,2 will present in 0-2(row) , 2(column) ; 2,2 will present in 0-2(row) , 1-2(column) etc and many more. 

# The most important formula which combines all the above miniature formula to one important one that is 
# Ans= N-1   M-1 
#      ∑     ∑      A[i][j]*(No of submatrix A[i][j] is part of )
#     i=0    j=0  

# Ans= N-1   M-1 
#      ∑     ∑      A[i][j]*(i+1)*(j+1)*(N-1)*(M-j)
#     i=0    j=0  


# Below is the code for the sub-matrices sum 
def Sum_of_all_Sub_Matrices_Sum(Mat):
    ans=0
    N=len(Mat)
    for i in range(N):                                              # Accessing the row 
        for j in range(N):                                          # Accessing the row elements (Columnar elements over the row)
            ans=ans+Mat[i][j]*(i+1)*(j+1)*(N-i)*(N-j)               # Using an ans variable to store the sum 
    return ans                                                      # Lastly returning them



Mat=[[1,2,3,3,4],[1,2,3,3,4],[1,2,3,3,4],[1,2,3,3,4],[1,2,3,3,4]]
result=Sum_of_all_Sub_Matrices_Sum(Mat)
print(result)