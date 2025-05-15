# Merge Overlapping Intervals
# Intervals -> start <= end
# l1           l2    
# (2,6)        (3,7)     0 1 2 3 4 5 6 7 8 
#                            2 3 4 5 6 
#                              3 4 5 6 7
#                              _______             from 3 to 6 the intervals elements are going to be merged
#
# (2,8)        (4,6)     0 1 2 3 4 5 6 7 8 9 
#                            2 3 4 5 6 7 8
#                                4 5 6
#                                _____             from 4 to 6 the interval elements are going to be merged
#
# (3,7)        (4,10)     0 1 2 3 4 5 6 7 8 9 10 
#                               3 4 5 6 7 
#                                 4 5 6 7 8 9 10
#                                 _______          from 4 to 7 the interval elements are going to be merged
#
# (3,6)        (6,10)     0 1 2 3 4 5 6 7 8 9 10 
#                               3 4 5 6 
#                                     6 7 8 9 10   from 6 to 6 the interval elements are going to get merged 
#
# (2,5)        (8,10)     0 1 2 3 4 5 6 7 8 9 10
#                             2 3 4 5     
#                                         8 9 10    No overlapping intervals
# 
# (5,8)        (1,3)     0 1 2 3 4 5 6 7 8 9 10 
#                          1 2 3   
#                                  5 6 7 8          No overlapping 
# 
# Below is the formula to check whether the given start and end of the both the index array is overlapping or not 
#
#                                       
# start 1  ----- > end 1                    if (start 2 > end 1  or start 1 > end 2 )
# start 2  ----- > end 2                    else overlapping 
# 
# Merge Interval ----> min(start 1 ,start 2) , max(end 1, end 2)
#
# if ( Start 2  >  end 1  or  start 1 > end 2 ) else overlapping 
# Below is the explanation for the above formula 
# Simply take an array of elements 0  1  2  3  4  5  6  7  8  9  10
# Intervals ( 2 , 5 ) ( 8 , 10 )         2--------5        8-----10
#             s1  e1    s2  e2           s1       e1       s2    e2 
# s2 is greater than e1 so it does overlaps each other 
# start 1 > end 2 if the start 1 and end 1 is next to start 2 and end 2 then this condition will help us to identify it 