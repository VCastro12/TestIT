# Your program will prompt the user to create at least one object of each type (Car and Pickup). Using a menu system and capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's attributes. The program will use user input to define the vehicle's attributes.
# A Vehicle class that contains all the methods and attributes outlined in the class diagram below.
# A Car class that is a child class of the Vehicle class with the methods and attributes detailed in the class diagram below. 
# A Pickup class is a child class of the Vehicle class with the methods and attributes detailed in the class diagram below. 

message = "Welcome to our virtual garage!!"
print(message)


class Vehicle:
  def _init_(self, make, model):
    self.make = make
    self.model = model
  def get_descriptive_name(self):
    print(f"{self.year} {self.make}")

pick = int(input("Enter 1 to make a car, \n2 to make a truck, or \n3 to quit: "))

if pick == 1:
  class Car(Vehicle):
    def _init_(self, make, model, doors):
      self.doors = doors
      super()._init_(make, model)
  input_make = input("Please enter the car make: ")
  input_model = input("Please enter the car model: ")
  input_doors = input("Please enter the number of doors: ")
elif pick == 2:
  class Truck(Vehicle):
    def _init_(self, make, model, bed_length):
      self.bed_length = bed_length
      super()._init_(make, model)
  input_make = input("Please enter the truck make: ")
  input_model = input("Please enter the truck model: ")
  input_bed_length = input("Please enter the bed length: ")
else:
  print("Goodbye.")





  



    

  