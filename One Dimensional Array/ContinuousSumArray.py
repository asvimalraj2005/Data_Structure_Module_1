# Initially all elements of an arr[N] are 0. Given Q queries 
# Every query contains [s,e,val]. Increment elements from s to e by val
# Return the final state of arr[]

# arr[]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# queries -> 3                
# s    e     val
# 3    6      3
# 2    7     -3
# 1    9      4  
#                             0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 
#                                         3   3   3   3
#                                    -3  -3  -3  -3  -3  -3 
#                                 4   4   4   4   4   4   4   4   4
#                 ans=        0   4   1   4   4   4   4   1   4   4

# query -> (i,j,x) -> (i,x)
#                  -> (j+1,-x)
def continuous_Sum_Query_2(query,arr):
    for i in range(len(query)):
        start_index=query[i][0]
        end_index=query[i][1]
        value=query[i][2]
        arr[start_index]=arr[start_index]+value
        if end_index< (len(arr)-1):
            arr[end_index+1]=arr[end_index+1]-value
    
    for i in range(1,len(arr)-1):
        arr[i]=arr[i]+arr[i-1]
    
    return arr

arr=[0,0,0,0,0,0,0,0,0,0]
query=[[3,6,3],[2,7,-3],[1,9,4]]
result=continuous_Sum_Query_2(query,arr)
print(result)
