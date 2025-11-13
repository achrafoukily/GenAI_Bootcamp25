#Exercise 1: Pets
#Instructions:
#Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
#See the example below, before diving in.
#Step 1: Create the Siamese class
#Step 2: Create a list of cat instances
#Step 3: Create a Pets instance of the list of cat instances
#sara_pets = Pets(all_cats)
#Step 4: Take cats for a walk
#sara_pets.walk()

class Pet:
    def __init__(self, all_cats):
        self.all_cats = all_cats
    def walk(self):
        for animal in self.all_cats:
            print(animal.walk())
    
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Siamese(Cat):
    pass
class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass


bengal_obj = Bengal("Whiskers", 3)
chartreux_obj = Chartreux("Luna", 2)
siamese_obj = Siamese("Oliver", 5)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pet(all_cats)
sara_pets.walk()


#Exercise 2 :

class Dog :
  def __init__(self,name,age,weight):
    self.name = name
    self.age = age
    self.weight = weight
  def barking(self):
    return f"{self.name} is barking"
  def running_speed(self):
    speed = self.weight / self.age * 10
    return speed
  def fighting(self,other_dog):
    dog_speed = self.running_speed()
    other_speed = other_dog.running_speed()
    if dog_speed > other_speed :
      return f"{self.name} is the winner"
    elif dog_speed < other_speed :
      return f"{other_dog.name} is the winner"
    else :
      return "Draw"
    

dog_1 = Dog("Rex",3,30)
dog_2 = Dog("Bella",4,25)
dog_3 = Dog("Buddy",2,38)
print(dog_1.barking())
print(f"The speed of {dog_1.name} is : {dog_2.running_speed()}")
print(dog_1.fighting(dog_3))

#Exercise 3 :
import random
from dog import Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        print(self.barking())
        self.trained = True
    
    def play(self, *args):
        dogs = [self.name] + [dog.name for dog in args]
        all_dogs = ", ".join(dogs)
        return f"{all_dogs} all play together"
    def do_a_trick(self):
      tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
      if self.trained == True :
        return random.choice(tricks)
      
dog_1 = Dog("Rex",3,30)
dog_2 = Dog("Bella",4,25)
my_dog = PetDog("Fido", 2, 10)  
my_dog.train()
print(my_dog.play(dog_1,dog_2))
print(my_dog.do_a_trick())


#Exercise 4 :

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def check_majority(self):
        if self.age >= 18:
            print(f"{self.first_name} you are over 18, your parents accept that you will go out with your friends")
        else:
            print(f"{self.first_name} Sorry, you are not allowed to go out with your friends.")
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        new_person = Person(first_name, self.last_name, age)
        self.members.append(new_person)
    
    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age}")


    

Benani = Family("Benani")

# Add members using born() method
Benani.born("Yassine", 45)
Benani.born("Ayman", 42)
Benani.born("Achraf", 16)
Benani.born("Ines", 20)

# Check majority for family members
Benani.members[0].check_majority()  
Benani.members[2].check_majority()  
Benani.members[3].check_majority()  

# Display family information
print()
Benani.family_presentation()
    