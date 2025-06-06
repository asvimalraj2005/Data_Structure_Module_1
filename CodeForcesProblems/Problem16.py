# ICPC Balloons 
# Prices for the teams -> whenever a team solves a problem that team gets the balloon
#                      -> The first to solve the problem will get an additional balloon
# 26 problems are in the contest that are labelled as A.B,C to Z (each of the 26 problem is labelled between A-Z )
# Input -> t test cases 
#       -> length of the string n and the string s containing the n characters inside it , i th character inthe string s denotes that problem from A-Z has been solved by some team 
#       -> No team will solve the same problem twice 
# Straigth forward approach observed from the input and output 
def Problem16():
    t=int(input())
    for _ in range(t):
        String=input().split()
        String_set=set(String)
        len_of_string=len(String)
        len_of_string_set=len(String_set)
        print(len_of_string+len_of_string_set)

Problem16()
        