x = 'Mike'
print(dir(x)) # Dir show e method of string Object
#Creating a Class
class Vehicle(object):
    """Docstring"""
#__init is special method create object based on this class.
# this method is only called once and not called again inside the program. 
 # it called as constructor   
    def __init__(self,color,doors,tires,type_of_vehicle):   
        """Constructor"""                                            
        self.color = color
        self.doors = doors
        self.tires = tires
        self.type_of_vehicle = type_of_vehicle

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" %self.type_of_vehicle

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" %(self.color,self.type_of_vehicle)                                                            
if __name__ =="__main__":
    #car instance of vehicle
    car = Vehicle("blue" , 5, 4,"car")
    print(car.brake())
    print(car.drive())
     #truck instance of vehicle
truck = Vehicle("red",3,5,"truck")
print(truck.drive())
print(truck.brake())

# Subclasses 

class Car(Vehicle):
    """
    The Car Class
    """
    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"
if __name__== "__main__":
    car = Car("yellow",2,4,"car")
    print(car.brake())
    print(car.drive())

