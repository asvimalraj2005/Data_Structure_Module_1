# This question is about Search in a row wise and column wise sorted matrix
# A matrix with the size of N*M will be given to you as A
# And an integer B will be given to target value in which you are going to find it in the row and column sorted array 
# The matrix will be sorted i.e every column and row will be sorted in non-decreasing order 
# For example here is an matrix which satisfies the condition 
# [ [ 1 , 2 , 3 , 4 , 5 ],           here you can see the left to right in the column is sorted
#   [ 6 , 7 , 8 , 9 , 10],           on the row wise the values here are sorted too 
#   [ 11, 12, 13, 14, 15],
#   [ 16, 17, 18, 19, 20],
#                          ]
# Now the target search = 18 if it is there we are going to return true if not we are going to return false
# The method or the approach we are going to use here is non-brute force method 
# let us take another 2d array as example 
#                 increasing            decreasing
#                 -->                  <--                                        # it's a memorising approach not logically implemented 
# increasing    ↓ [  [ -5 , -2  ,  1 ,  13 ]    ↓  increasing
#                    [ -4 ,  0  ,  3 ,  14 ]                                      From the observation increasing-increasing, decreasing-decreasing start points on the top left corner and bottom right most corner is not used for iteration purpose 
#                    [ -3 ,  2  ,  5 ,  18 ]                                      whereas the increasing-decreasing, decreasing-increasing will be used as the start point 
# decreasing    ↑    [  2 ,  6  ,  10, 20  ]  ] ↑  decreasing                     in-here let take the right top most element and the search element is 6 
#                 -->                   <--                                       From 13 we are gonna iterate -> 13 is greater than 6 so we decrease moving to the left side
#                 increasing            decreasing                                                             -> 1 is smaller than 6 so we increase moving towards to the down side    
#                                                                                                              -> 5 is smaller than 6 so we increase moving towards to the down side 
#                                                                                                              -> 10 is greater than 6 so we decrease moving towards to the left side 
#                                                                                                              -> 6==target so we stop here and then return the index of it or we return 1 or -1 if is not found inside the 2d matrix 
# Below is the python code for the above passage 
def search_sorted_row_column(Matrix,Target):
    ans=0
    N=len(Matrix)
  
    element_column_counter=0                                    # Initialising the column traversing counter 
    right_most_element_index=0                                  # Initialising the column element index varaible to store the last element index of the first row 
    while element_column_counter<len(Matrix[0]):                # Since we know the column end'th len 
        right_most_element=Matrix[0][element_column_counter]    # The element variable 'right_most_element' store the top rightmost element of the array
        right_most_element_index=element_column_counter        
        element_column_counter=element_column_counter+1         # Incrementing the counter variable 'element_column_counter' by 1 
         
                                                                # Now we the right top most element and it's index 
                                                                # Now we initialising two counters one is row(increasing) and other one is for column(decreasing) with the help of pointers 
    row_pointer=0                                               # Row_pointer
    column_pointer=right_most_element_index                     # Column_Pointer
    while(row_pointer<N and column_pointer>=0):                # Running a loop while row_pointer reaches N and column pointer which starts from right until we reach the left end 
        if Matrix[row_pointer][column_pointer]==Target:         # Checking if the row index i,j element is equal to the targer or not 
            return True                                         # Returning true if it is exist 
        elif Matrix[row_pointer][column_pointer]>Target:          # We are decreasing the column pointer by 1 since it is greater than target value so we should move left 
            column_pointer=column_pointer-1 
        else:   
            row_pointer=row_pointer+1                           # If it smaller we are increasing 
    
    return False 


Matrix=[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,34,35,36,37]]
target=100
result=search_sorted_row_column(Matrix,target)
print(result)
        
            
        
    
    