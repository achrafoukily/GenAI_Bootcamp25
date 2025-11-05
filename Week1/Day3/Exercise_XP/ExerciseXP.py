#Exercise 1: Converting Lists into Dictionaries
#Key Python Topics:
#Creating dictionaries
#Zip function or dictionary comprehension
#Instructions
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = {}

for key,value in zip(keys,values):
  dictionary[key] = value
    

print(dictionary)

#Exercise 2: Cinemax #2
#Key Python Topics:
#Looping through dictionaries
#Conditionals
#Calculations
#Instructions
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Family members' ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15
#Family Data:
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#Loop through the family dictionary to calculate the total cost.
#Print the ticket price for each family member.
#Print the total cost at the end.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost =[]
a = 10
b = 15

for key,value in family.items():
  if value < 3 :
    print(f'the ticket price for {key} is : {0}$')
  elif 3 <= value <= 12 :
    print(f"the ticket price for {key} is : {10}$")
  elif value > 12 :
    print(f"the ticket price for {key} is : {15}$")

for key,value in family.items() :
  if value > 12 : 
    cost.append(b)
  elif 3<=value<=12 : 
    cost.append(a)

print(f"the total cost is : {sum(cost)}")

#Bonus:
#Allow the user to input family members’ names and ages, then calculate the total ticket cost.

names = []
ages = []

while True :
  name = input("enter the name of the family member : ")
  if name.lower() != "quit"  :
    names.append(name)
    age = int(input("enter the age of the family member : "))
    ages.append(age)
  elif name.lower() == "quit"  :
    break

family_members = {}

for key,value in zip(names,ages):
  family_members[key] = value

print(family_members)

cost =[]
b = 10
c = 15

for key,value in family_members.items() :
  if 3<=value<=12 : 
    cost.append(b)
  elif value > 12 : 
    cost.append(c)

print(f"the total cost is : {sum(cost)}")

#Exercise 3: Zara
#Key Python Topics:
#Creating dictionaries
#Accessing and modifying dictionary elements
#Dictionary methods like .pop() and .update()
#Instructions
#Create and manipulate a dictionary that contains information about the Zara brand.
#Brand Information:
#name: Zara
#creation_date: 1975
#creator_name: Amancio Ortega Gaona
#type_of_clothes: men, women, children, home
#international_competitors: Gap, H&M, Benetton
#number_stores: 7000
#major_color: 
#    France: blue, 
#    Spain: red, 
#    US: pink, green
#Create a dictionary called brand with the provided data.
#Modify and access the dictionary as follows:
#Change the value of number_stores to 2.
#Print a sentence describing Zara’s clients using the type_of_clothes key.
#Add a new key country_creation with the value Spain.
#Check if international_competitors exists and, if so, add “Desigual” to the list.
#Delete the creation_date key.
#Print the last item in international_competitors.
#Print the major colors in the US.
#Print the number of keys in the dictionary.
#Print all keys of the dictionary.

brand = {"name": "Zara",
"creation_date": 1975
, "creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color": 
    {"France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]}}

brand["number_stores"] = 2
print(brand)
print(f"Zara is a brand that serve all categories : {brand["type_of_clothes"][0]} , {brand["type_of_clothes"][1]} , {brand["type_of_clothes"][2]} and {brand["type_of_clothes"][3]}")
brand["country_creation"] = "Spain"
for key,value in brand.items() :
  if key == "international_competitors" :
    value.append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())    

#Bonus:
#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {"creation_date": 1975, "number_stores": 7000}
print(more_on_zara)
print(brand)
brand.update(more_on_zara)
print(brand)

#Exercise 4: Disney Characters
#Key Python Topics:
#Looping with indexes
#Dictionary creation
#Sorting
#Instructions
#You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
#Character List:
#users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#Expected Results:
#1. Create a dictionary that maps characters to their indices:
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#2. Create a dictionary that maps indices to characters:
#{0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#Create a dictionary that maps characters to their indices:
user_index = {}
index = list(range(len(users)))
for key,value in zip(users,index):
  user_index[key] = value
print(user_index)

#Create a dictionary that maps indices to characters:
user_index_1 = {}
for key,value in enumerate(users):
  user_index_1[key] = value
print(user_index_1)

#Create a dictionary where characters are sorted alphabetically and mapped to their indices:
users_sorted = sorted(users)
index_sorted = list(range(len(users_sorted)))
user_index_2 = {}
for key,value in zip(users_sorted,index_sorted):
  user_index_2[key] = value
print(user_index_2)

