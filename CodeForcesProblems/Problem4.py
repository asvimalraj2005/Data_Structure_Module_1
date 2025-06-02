# Sometimes some words like "localization" or "internationalization" are so long that writing them many times 
# in one text is quite tiresome.Let's consider a word too long, if its length is strictly more than 10 characters.
# All too long words should be replaced with a special abbreviation. This abbreviation is made like this: we write down the 
# first and the last letter of a word and between them we write the number of letters 
# between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.
# Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".
# You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be 
# replaced by the abbreviation and the words that are not too long should not undergo any changes.
# Input
# The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of 
# lowercase Latin letters and possess the lengths of from 1 to 100 characters.
# Output
# Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.
def Word_Solution(words):                                                   # Words are passed here
    result = []                                                             # Abbreviated words are stored in this array 
    for word in words:                                                      # Iterating over the string 
        if len(word) > 10:                                                  # If the word has the length greater than 10
            abbreviation = word[0] + str(len(word) - 2) + word[-1]          # The first character and last character of the word be appended to the abbreviation, in the middle of those two character the length of the string with subtraction of these two character length will be stored 
            result.append(abbreviation)                                     # Appending to the list 
        else:
            result.append(word)                                             # If is not greater than length 10 we are appending to the result list itself 
    return result                                                           # Returning the list 

n = int(input())                                                            # No of input 
words = [input().strip() for _ in range(n)]                                 # Creating a list named words with list comprehension placed inside 
for word in Word_Solution(words):                                           # Passing the input to the Word_Solution method 
    print(word)                                                             # Returning from there and printing here 
