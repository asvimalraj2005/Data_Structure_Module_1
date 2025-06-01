# Word
# Nigel is very upset that many people on the Net mix uppercase and lowercase letters in one
# word. That's why he decided to invent an extension for his favourite browser that would change
# the letter's register in every word so that it either only consisted of lowercase letters or, vide 
# versa, only of uppercase ones. At that as little as possible letters should be changed in the word.
# For example, the word HoUse must be replaced with house, and the word ErE wirh ere. If a word contains 
# an equal number of uppercase and lowercase letters, you should replace all the ltters with lowercase ones.
# For example maTRIx should be replaced by matrix. Your task is to use the given method on one given word 
# Problem Solution
def Word(A):
    count_up=0                          # Used to count the uppercase characters 
    count_low=0                         # Used to count the lowercase characters
    for ch in A:                        # By using the loop we are traversing the string 
        if ch.islower():                # if the string character is lowercase we are incrementing the count_low by 1   
            count_low=count_low+1
        elif ch.isupper():              # if the string character is uppercase we are incrementing the count_up by 1
            count_up=count_up+1
    if count_low>=count_up:             # Conditional check if the lowercase character count is high we are modifying the string to lowercase 
        return A.lower()
    else:                               # if not uppercase 
        return A.upper()


https://codeforces.com/problemset/problem/59/A
    

    
    
