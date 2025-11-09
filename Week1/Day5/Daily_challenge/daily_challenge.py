#Challenge 1: Sorting
#Instructions:
#Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

#Step 1: Get Input
#Use the input() function to get a string of words from the user.
#The words will be separated by commas.

#Step 2: Split the String

#Step 3: Sort the List

#Step 4: Join the Sorted List

#Step 5: Print the Result
#Print the resulting comma-separated string.

word = input("Enter a words separated by coma : ")
words = word.split(",")
sort = sorted(words)
coma = " , "
result = coma.join(sort)
print(f"{result} . ")

#Challenge 2: Longest Word
#Instructions:
#Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.

#Step 1: Define the Function
#Define a function that takes a string (the sentence) as a parameter.

#Step 2: Split the Sentence into Words

#Step 3: Initialize Variables

#Step 4: Iterate Through the Words

#Step 5: Compare Word Lengths

#Step 6: Return the Longest Word

def longest_word(sentence):
  words = sentence.split()
  long_word = []
  for word in words :
    if len(word) == max(map(len, words)):
      long_word.append(word)
      
  print(long_word[0])

inp = input("enter your sentence : ")
longest_word(inp)