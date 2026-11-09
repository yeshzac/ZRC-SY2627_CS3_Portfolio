# a. What is duck typing, as explained in the video?

# Duck typing is a concept in dynamic programming where an object's suitability is determined by the presence of certain methods and properties,
# rather than the object's actual inherited type. 

# b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

# The Car class needed to implement a method with the same name and signature as the animals' method (e.g., make_sound()), even though its
# internal behavior would be completely different.

# 3. How does the code in 2.2 demonstrate polymorphism?
# The code demonstrates polymorphism (specifically via duck-typing) because the start_trip() function can accept any
# object (Car, Boat, or Drone) as long as it has a .move() method. The function does not need to know the specific
# class type beforehand; it simply invokes vehicle.move(), and Python handles the correct method execution
#  dynamically based on whichever object is passed.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car_obj = Car()
boat_obj = Boat()
drone_obj = Drone()

start_trip(car_obj)
start_trip(boat_obj)
start_trip(drone_obj)