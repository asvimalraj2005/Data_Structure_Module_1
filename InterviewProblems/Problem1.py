# Problem statement -> Given a sorted list of overlapping intervals, sorted based on start-time, Merge all 
# Overlapping intervals and return the sorted list of non-overlapping intervals
# In simplified manner sorted list of overlapping intervals(start to end) are given to us as a input 
# The interval list looks like this 
#    
# Interval list                  Array       0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 
# start     End                     
#   1        2                                  1__2
#   1        4                                  1________4
#   5        6                                              5__6
#   6        7                                                 6__7
#   7        10                                                   7________10
#   8        9                                                       8__9
#   12       14                                                                    12______14
#
#               The output will look like       1________4  5______________10      12______14
# 
# Intervals[N] -> [ (0,2) , (1,4) , (5,6) , (6,8) , (7,10) , (8,9) , (12,14) ]
#                    0       1       5       6       7        8       12 
# Interval connection 
# Output will be ->  0-------->4     5------------------------>10    12--->14
#
# start(i+1) >= start i , for all i ------> if (start (i+1) <= end i)  ==> Overlapping          <---- This is an formula used in this approach for the problem
# Below is the python code 
#
#
def MergeInterval(Intervals,Array):                             # Passing the Interval list                                          00  01
    Start_index=Intervals[0][0]                                 # Storing the Start Index      0,0                                   10  11
    End_index=Intervals[0][1]                                   # Storing the end Index        0,1                                   20  21
    N=len(Array)                                                # Using N variable to store the length of the interval list          30  31
    for i in range(1,N):                                        # Running the loop from the 1st row because we are stored the row one start index and end index 
        if(Intervals[i][0] <= End_index):                       # Checking if the start index(Interval[i][0]) is less than or equal to end index
            End_index=max(End_index,Intervals[i][1])            # If does get satisfied we are updating end index by comparing the end index value and the iterating 01,11,21,31 values of the 2d interval list 
        else:                                                   # The above condition is to expand the end index only so we can compare the intervals and provide the appropriate start index and end index of the intervals 
            print(Start_index," , ",End_index)                  # Printing the start index and end index if the 'if condition is not get satisified' of the overall merging intervals   
            Start_index=Intervals[i][0]                         # Updating the start index 
            End_index=Intervals[i][1]                           # Updating the end index
    print(Start_index," , ",End_index)                          


Intervals=[[1,2],[1,4],[5,6],[6,7],[7,10],[8,9]]

result=MergeInterval(Intervals)
print(result)
    

