#Challenge 1: Multiples of a Number

#Key Python Topics:
#input() function
#Loops (for or while)
#Lists and appending items
#Basic arithmetic (multiplication)
#Instructions:a
#1. Ask the user for two inputs:
#A number (integer).
#A length (integer).
#2. Create a program that generates a list of multiples of the given number.
#3. The list should stop when it reaches the length specified by the user.

#Example 1:
#Input:
#number: 7
#length: 5
#Output:
#[7, 14, 21, 28, 35]

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))
output = list()
m = 1
while True :
  if m <= length :
    multiplication = number * m
    output.append(multiplication)
    m += 1
  else :
    print(output)
    break
  
#Challenge 2: Remove Consecutive Duplicate Letters

#Key Python Topics:
#input() function
#Strings and string manipulation
#Loops (for or while)
#Conditional statements (if)

#Instructions:
#1. Ask the user for a string.
#2. Write a program that processes the string to remove consecutive duplicate letters.
#The new string should only contain unique consecutive letters.
#For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
#3. The program should print the modified string.

#Example 1:
#Input:
#user’s word: "ppoeemm"
#Output:
#"poem"
#Notes:
#The final string will not include any consecutive duplicates, but non-consecutive duplicates are allowed.
#Example: In "recursive", the two ‘r’s and two ‘e’s are allowed because they are not consecutive.

string = input("Enter a string : ")
none_dup = list()
none_dup.append(string[0])
l = 1
for l in range(len(string)) :
  if string[l] != string[l-1]:
    none_dup.append(string[l])

print(none_dup)
  