# The file is about Continuous Sum Query 
# Initially all elements of an arr[N] are 0. Then you are given Q queries. Every query contains
# i-idx and value. Increment elements from ith.idx to last idx by value. Return final state of arr[]
#                               0,1,2,3,4,5,6
# Queries -> 3        arr[] -> [0,0,0,0,0,0,0]
#   idx   val                         
#    3     4                          4,4,4,4
#    1     3                      3,3,3,3,3,3
#    4    -2                           -2,-2,-2
#    ans                        0,3,3,7,5,5,5

# Add x from i to (N-1) -> Prefix Sum 

def Continuous_Sum_Query(query,arr):
    for i in range(len(query)-1):
        idx=query[i][0]
        val=query[i][1]
        arr[idx]=arr[idx]+val
    
    for i in range(1,len(arr)-1):
        arr[i]=arr[i]+arr[i-1]
    
    return arr


arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
query=[[1,2],[3,4],[3,5]]
result=Continuous_Sum_Query(query,arr)
print(result)
