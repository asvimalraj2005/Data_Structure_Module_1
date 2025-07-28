SCALER organizes a series of contests aimed at helping learners enhance their coding skills. Each learner can participate in multiple contests, and their participation is represented by integers in an array. The goal is to identify how frequently each learner has participated in these contests. This information will help SCALER determine which learners are participating the least, allowing them to provide targeted support and encouragement.


Given an array A that represents the participants of various contests, where each integer corresponds to a specific learner, and an array B containing the learners for whom you want to check participation frequency, your task is to find the frequency of each learner from array B in the array A and return a list containing all these frequencies

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    ans=[]
    def solve(self, A, B):
        # B contains the student's id as integer 
        # A contains the no of participation they have done 
        # Map B with A participations 
        # 
        return ans 

    def contains(self,A):
        index=self.hashfunction(A)
        bucket=self.A[index]
        for key,value in bucket:
            if key==A:
                ans.append(ans)          
    
    def hash_fucntion(self,A):
        key_string=str(A)
        hash_result=0
        for c in key_string:
            hash_result=(hash_result*31+ord(c))%A.len() 



