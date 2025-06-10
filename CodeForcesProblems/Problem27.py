# https://codeforces.com/problemset/problem/1398/C
# Below is the code for the above problem statement link
def Problem27():
    t=int(input())
    for _ in range(t):
        n=int(input())          # <- Length of the array 
        s=input()
        num_array=list(map(s.split()))
        print(num_array)
        sum_var=0
        index_var=0
        count=0
        for i in range(len(num_array)):
            for n in range(i,len(num_array)):
                for m in range(i,n):
                    sum_var=sum_var+num_array[m]
                    index_var=index_var+m
                if sum_var==index_var:
                    count=count+1
    print(count)

Problem27()
                

        