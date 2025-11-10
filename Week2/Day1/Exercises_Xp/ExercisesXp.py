#Exercise 1: Cats
#Instructions:
#Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

#Step 1: Create Cat Objects
#Use the Cat class to create three cat objects with different names and ages.

#Step 2: Create a Function to Find the Oldest Cat
#Create a function that takes the three cat objects as input.
#Inside the function, compare the ages of the cats to find the oldest one.
#Return the oldest cat object.

#Step 3: Print the Oldest Cat’s Details
#Call the function to get the oldest cat.
#Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
#Replace <cat_name> and <cat_age> with the oldest cat’s name and age.


class Cat :

  def __init__(self,cat_name,cat_age):
    self.name = cat_name 
    self.age = cat_age
    

def find_oldest_cat(cat_1, cat_2, cat_3):
  oldest_cat = max(cat_1.age, cat_2.age, cat_3.age)
  if oldest_cat == cat_1.age :
    print(f"The oldest cat is : " , cat_1.name)
  elif oldest_cat == cat_2.age :
    print(f"The oldest cat is : " , cat_2.name)
  elif oldest_cat == cat_3.age :
    print(f"The oldest cat is : " , cat_3.name)

  
cat_1 = Cat("bob",5)
cat_2 = Cat("mia",7)
cat_3 = Cat("tom",3)
find_oldest_cat(cat_1,cat_2,cat_3)

#Exercise 2 : Dogs
#Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.
#Instructions:
#Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

#Step 1: Create the Dog Class
#Create a class called Dog.
#In the __init__ method, take name and height as parameters and create corresponding attributes.
#Create a bark() method that prints “<dog_name> goes woof!”.
#Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

#Step 2: Create Dog Objects
#Create davids_dog and sarahs_dog objects with their respective names and heights.

#Step 3: Print Dog Details and Call Methods
#Print the name and height of each dog.
#Call the bark() and jump() methods for each dog.

#Step 4: Compare Dog Sizes


class Dog :
  
  def __init__(self,name,height):
    self.name = name
    self.height = height
  
  def bark(self):
    print(self.name , "goes woof!!")

  def jump(self):
    x = self.height * 2
    print(self.name ,"jumps" , x , "cm high!!!")

david_dog = Dog("David_dog",50)
sarah_dog = Dog("Sarah_dog",60)

david_dog.bark()
david_dog.jump()
sarah_dog.bark()
sarah_dog.jump()
def size_comparaison(david_dog,sarah_dog):
  if david_dog.height > sarah_dog.height :
    print("David's dog size is bigger than Sarah")
  else :
    print("Sarah's dog size is bigger than David")

size_comparaison(david_dog,sarah_dog)

#Exercise 3 : Who’s the song producer?
#Goal: Create a Song class to represent song lyrics and print them.
#Instructions:
#Create a Song class with a method to print song lyrics line by line.

#Step 1: Create the Song Class
#Create a class called Song.
#In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
#Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

class Song :
  def __init__(self,lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics :
      print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo
#Goal:
#Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
#Instructions
#Step 1: Define the Zoo Class
#1. Create a class called Zoo.
#2. Implement the __init__() method:
#It takes a string parameter zoo_name, representing the name of the zoo.
#Initialize an empty list called animals to keep track of animal names.
#3. Add a method add_animal(new_animal):
#This method adds a new animal to the animals list.
#Do not add the animal if it is already in the list.
#4. Add a method get_animals():
#This method prints all animals currently in the zoo.
#5. Add a method sell_animal(animal_sold):
#This method checks if a specified animal exists on the animals list and if so, remove from it.
#6. Add a method sort_animals():
#This method sorts the animals alphabetically.
#It also groups them by the first letter of their name.
#The result should be a dictionary where:
#Each key is a letter.
#Each value is a list of animals that start with that letter.
#7. Add a method get_groups():
#This method prints the grouped animals as created by sort_animals().
#Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, you can pass multiple animals names separated by a comma.

class Zoo :
  def __init__(self,zoo_name):
    self.zoo_name = zoo_name
    self.animals = []

  def add_animal(self,*new_animal):
    for animal in new_animal :
      if animal not in self.animals :
        self.animals.append(animal)

  def get_animals(self):
    print("The animals in the zoo are : " , self.animals)
  
  def sell_animal(self,animal_sold):
    if animal_sold in self.animals:
      self.animals.remove(animal_sold)

  def sort_animals(self):
    self.animals.sort()  
    self.dictionary = {}

    for animal in self.animals:
      if animal[0] not in self.dictionary:
        self.dictionary[animal[0]] = []
        self.dictionary[animal[0]].append(animal)
      elif animal[0] in self.dictionary:
        self.dictionary[animal[0]].append(animal)

    return self.dictionary

  def get_groups(self):
    for key,value in self.dictionary.items():
      print(key,value)
    

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Lion","Giraffe","Bear","Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()


