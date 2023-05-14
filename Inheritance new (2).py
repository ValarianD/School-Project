class vehicle:


    def setVehicle_Make(self, make):
      self.vehicle_make = make


    def setVehicle_Model(self, model):
      self.vehicle_model = model

    def displayOption(self):
      print(f"The vehicle make is {self.vehicle_make}")
      print(f"The vehicle model is {self.vehicle_model}")



class car(vehicle):


  def setCar_Door(self, door):
    self.car_door = door


  def displayOption(self):
    print(f"The number of doors is {self.car_door}.")
    print(f"The vehicle make is {self.vehicle_make}.")
    print(f"The vehicle model is {self.vehicle_model}.")



class truck(vehicle):


  def setBed_Length(self, length):
    self.bed_length = length


  def displayOption(self):
    print(f"The bedlength is {self.bed_length}.")
    print(f"The vehicle make is {self.vehicle_make}.")
    print(f"The vehicle model is {self.vehicle_model}.")



input_car = input("Please enter the car name: ")
input_make = input("Please enter the make: ")
input_model = input("Please enter the model: ")
input_doors = input("Please enter the number of doors: ")

new_car = car()
new_car.setCar_Door(input_doors)
new_car.setVehicle_Make(input_make)
new_car.setVehicle_Model(input_model)
new_car.displayOption()



input_truck = input("\nPlease enter the name of the truck: ")
input_truck_make = input("Please enter the make: ")
input_truck_model = input("Please enter the truck model: ")
input_bed_length = input("Please enter the bedlength: ")

new_truck = truck()
new_truck.setBed_Length(input_bed_length)
new_truck.setVehicle_Make(input_truck_make)
new_truck.setVehicle_Model(input_truck_model)
new_truck.displayOption()

prompt = input("Press enter to exit.")

# Professor Voelcker's algorithim was used in this program. 
  
    
    
    
    
    



  