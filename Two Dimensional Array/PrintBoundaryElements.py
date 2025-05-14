# The definition is to print the boundary elements of the given 2 Dimensional array 
# Given example [ [1,2,3,4],             The boundary elements for the 2 Dimensional array 1,2,3,4
#                 [1,2,3,4],                                                               1     4
#                 [1,2,3,4],                                                               1     4
#                 [1,2,3,4] ]                                                              1,2,3,4
# Below is the python code to implement the approach 
def PrintSpriral(Mat):
    N=len(Mat)                         #                                                  -->     
    for i in range(len(Mat)):          # This loop will print the first row              1 2 3 4         
        print(Mat[0][i],end=' ')       #                                                                    4
    for i in range(1,len(Mat)):        # This loop will print the right column                              4      (Downward)
        print(Mat[i][N-1],end=' ')     #                                                                    4
    for i in range(N-2,-1,-1):         # This loop will print the last column            1 2 3 4
        print(Mat[N-1][i],end=' ')     #                                                  <-- 
    for i in range(N-2,0,-1):          # This loop will print the left colum                                1
        print(Mat[i][0],end=' ')       #                                                                    1       (Upward)
                                       #                                                                    1
                                       #                                                                    1

Mat=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

result_print_spiral=PrintSpriral(Mat)
print(result_print_spiral)