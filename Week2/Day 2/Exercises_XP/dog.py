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
