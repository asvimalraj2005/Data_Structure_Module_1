# Boring Apartments 
# https://codeforces.com/problemset/problem/1433/A 
# Straight forward 
# Below is the code 
def Problem14():
    boring_apartments=[[1,11,111,1111],
                       [2,22,222,2222],
                       [3,33,333,3333],
                       [4,44,444,4444],
                       [5,55,555,5555],
                       [6,66,666,6666],
                       [7,77,777,7777],
                       [8,88,888,8888],
                       [9,99,999,9999]]
    # Observed : if the resident of boring apartment 22 answered, then our character called apartments with numbers 1,11,111,111,2,22 and the total number of digits he pressed is 1+2+3+4+1+2=13 
    t=int(input())
    for _ in range(t):
        boring_number=int(input())
        total_no=0
        found=False
        for i in range(len(boring_apartments)):
            for j in range(len(boring_apartments[i])):
                total_no=total_no+len(str(boring_apartments[i][j]))
                if boring_apartments[i][j]==boring_number:
                    found=True
                    break
            if found:
                break
        print(total_no)
        
Problem14()

        
