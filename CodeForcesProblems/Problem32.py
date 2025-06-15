# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

pick = 20

def guess(num: int) -> int:
    if num>pick:
        return -1
    elif num<pick:
        return 1
    else:
        return 0

def guessNumber(n: int) -> int:
    left, right = 1, n
    while left<=right:
        mid=(left+right) // 2
        res=guess(mid)
        
        if res==0:
            return mid
        elif res<0:
            right=mid-1
        else:
            left=mid+1
    
    return -1  


n = 10
result = guessNumber(n)
print(f"Guessed number is: {result}")
