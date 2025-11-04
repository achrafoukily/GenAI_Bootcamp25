#Exercise 1: Favorite Numbers
#Key Python Topics:

#Sets
#Adding/removing items in a set
#Set concatenation (using union)

#Instructions:

#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {2,3,7,9}
my_fav_numbers.update([5,4])
my_fav_numbers.remove(4)
friend_fav_numbers = {2,4,9,3,6,5}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2: Tuple
#Key Python Topics:

#Tuples (immutability) 
#Instructions:

#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

a = (1,9,3,6,3)
b = list(a)
b.extend([6,4,2])
a = tuple(b)
print(a)

#Exercise 3: List Manipulation
#Key Python Topics:

#Lists
#List methods: append, remove, insert, count, clear
#Instructions:

#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.

basket = ["Banana","Apples","Oranges","Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
basket.count("Apples")
basket.clear()
print(basket)

#Exercise 4: Floats
#Key Python Topics:

#Lists
#Floats and integers
#Range generation
#Instructions:

#Recap: What is a float? What’s the difference between a float and an integer?
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.
#Think: Can you generate this sequence using a loop or another method?

a = []
n = 1.5
while n <= 5 :
  a.append(n)
  n += 0.5
print(a)

#Exercise 5: For Loop
#Key Python Topics:

#Loops (for)
#Range and indexing

#Instructions:

#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.

for n in range(1,21) :
  print(n)

for n in range(1,21,2) :
  print(n)

#Exercise 6: While Loop
#Key Python Topics:

#Loops (while)
#Conditionals
#Instructions:

#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop

name = input("Enter your name")
while True :
  if name.isdigit() or len(name)<3 :
    print("Incorrect answer , please try again")
    name = input("Enter your name")
  else :
    print("Thank you")
    break

#Exercise 7: Favorite Fruits
#Key Python Topics:

#Input/output
#Strings and lists
#Conditionals
#Instructions:

#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"

favorite_fruits = input("Enter your favorite fruits :").lower()
favorite_fruits = list(favorite_fruits.split())
print(favorite_fruits)
user_fruit = input("Enter a fruit name : ").lower()
if user_fruit in favorite_fruits :
  print("You chose one of you favorite fruits! Enjoy!")
else :
  print("You chose a new fruit.I hope you enjoy it!")

#Exercise 8: Pizza Toppings
#Key Python Topics:

#Loops
#Lists
#String formatting
#Instructions:

#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings = input("Enter pizza toppings one by one and enter quit when you finish : ").lower()
pizza_toppings = list()
while True :
  if toppings != "quit" :
    pizza_toppings.insert(0,toppings)
    print(f"Adding {toppings} to your pizza")
    toppings = input("Enter pizza toppings one by one and quit when you are finished : ").lower()
  elif toppings == "quit" :
    break
print(f" All the toppings :{pizza_toppings}")
cost = 10 + 2.5*len(pizza_toppings)
print(f"The total cost is :{cost}$")  

#Exercise 9 : Cinemax Tickets
#Key Python Topics:

#Conditionals
#Lists
#Loops
#Instructions:

#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.

age = input("Enter the age of each person of your family , and quit when you finish :")
cost = list()
while True :
  if age.isdigit():
    if int(age) <= 3 :
      age = input("Enter the age of each person of your family , and quit when you finish :")
    elif 3 < int(age) <= 12 :
      cost.append(10)
      age = input("Enter the age of each person of your family , and quit when you finish :")
    elif  int(age) > 12 :
      cost.append(15)
      age = input("Enter the age of each person of your family , and quit when you finish :")
  elif age.lower() == "quit" :
    print(f"The final cost is : {sum(cost)}")
    break

#Bonus:

#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.

age = input("Eneter your age / quit : ")
attendees = list()
while True :
  if age.isdigit() :
    if 16 <= int(age) <= 21 :
      attendees.append(age)
      age = input("Enter your age : ")
    else :
      age = input("Enter your age : ")
  elif age.lower() == "quit" :
    print(f"The final list of attendees is : {attendees}")
    break


  

