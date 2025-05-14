# Given a Number to you as A, you should form a square matrix with the values which are upto or equal to A^2
# For example you are given a number 6 
# Then the matrix will get formed as 
# [ [ 1 , 2 , 3 , 4 , 5 , 6 ] ,
#   [ 20 , 21 , 22, 23, 24, 7 ]  ,
#   [ 19 , 32 , 33 , 34 , 25 , 8 ],
#   [ 18 , 31 , 36 , 35 , 26 , 9 ],
#   [ 17 , 30 , 29 , 28 , 27 , 10 ],
#   [ 16 , 15 , 14 , 13 , 12 , 11] ]
#  This is how the square matrix looks like 
def Spiral_Matrix(A):
    ans_matrix=[[]]*(A*A)
    N=len(A)
    for i in range(len(A)):            # Going to get executed until A times
        
        # Top most layer of the matrix variable
        top_layer_row_variable=0
        top_layer_column_variable=0
        end_number_top_layer=0
        for j in range(N):
            ans_matrix[top_layer_row_variable][top_layer_column_variable]=j
            top_layer_column_variable=top_layer_column_variable+1
            end_number_top_layer=j
        top_layer_column_variable=top_layer_column_variable+1
        
        # Right most column filling loop
        end_number_right_column=end_number_top_layer
        right_most_row_variable=top_layer_column_variable
        right_most_column_variable=A-1
        
        for k in range(N):
            ans_matrix[right_most_row_variable][right_most_column_variable]=end_number_top_layer
            right_most_row_variable=right_most_row_variable+1
            end_number_right_column=end_number_right_column+1
        

        # Bottom layer row filling loop 
        bottom_layer_row_variable=right_most_row_variable
        bottom_layer_column_variable=N-2
        end_number_bottom_layer=end_number_right_column
        for m in range(N):
            ans_matrix[bottom_layer_row_variable][bottom_layer_column_variable]=end_number_bottom_layer
            bottom_layer_column_variable=bottom_layer_column_variable-1
            end_number_bottom_layer=end_number_bottom_layer+1
            
        # Left column layer filling loop 
        left_layer_row_variable=bottom_layer_row_variable
        left_layer_column_variable=0
        left_layer_end_number=end_number_bottom_layer
        for n in range(N):
            ans_matrix[left_layer_row_variable][left_layer_column_variable]=left_layer_end_number
            left_layer_row_variable=left_layer_row_variable-1
            left_layer_end_number=left_layer_end_number+1
        N=N-1
        
        
            
        
            
            
        