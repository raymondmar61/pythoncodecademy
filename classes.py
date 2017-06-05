#Defining a class is much like defining a function, but we use the class keyword instead. We also use the word object in parentheses because we want our classes to inherit the object class. This means that our class has all the properties of an object, which is the simplest, most basic class.
#An empty class would look like this: class ClassName(object): # class statements go here
class Car(object):
#Classes can have member variables that store information about each class object. We call them member variables since they are information that belongs to the class object.  memberVariable = "InitialValue"
	condition = "new"
#There is a special function named __init__() that gets called whenever we create a new instance of a class. It exists by default, even though we don't see it. 
#However, we can define our own __init__() function inside the class, overwriting the default version, and add more variables.
#The first argument passed to __init__() must always be the keyword self - this is how the object keeps track of itself internally, and we can pass additional variables after that.
	def __init__(self, model, color, mpg):
#In order to assign a variable to the class (creating a member variable), we use dot notation.	self.new_variable = new_variable
		self.model = model
		self.color = color
		self.mpg = mpg
#Besides member variables, classes can also have their own methods.	You need to provide self as the first argument of any class method.
#Inside the Car class, add a method named display_car() to Car that will reference the Car's member variables to return the string, "This is a [color] [model] with [mpg] MPG." You can use the str() function to turn your mpg into a string when creating the display string.
	def display_car(self):
		print("This is a %s %s with %s MPG." % (self.color, self.model, self.mpg))
#We can modify variables that belong to a class the same way that we initialize those member variables; in this case, condition = "new" variable.  This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.  Use self. notation.  
	def drive_car(self):
		self.condition = "used"
		return self.condition
#Inheritance.  We can create more complicated classes that inherit variables or methods from their parent classes. This saves us time and helps us build more complicated objects, since these child classes can also include additional variables or methods.
#We define a "child" class that inherits all of the variables and functions from its "parent" class like so:  class ChildClass(ParentClass):  # new variables and functions go here
class ElectricCar(Car):
	def __init__(self, model, color, mpg, battery_type):
		super(ElectricCar, self).__init__(model, color, mpg)
		self.battery_type = battery_type
	def display_electriccar(self):
		print(self.battery_type, self.color, self.mpg, self.model)
	def drive_car(self):
		condition = "like new"
		return condition	
#We can use classes to create new objects, which we say are instances of those classes.  newObject = ClassName()
my_car = Car("DeLorean","silver",88)
#Since we've created an object my_car that is an instance of the Car class, my_car should already have a member variable named condition. This attribute gets assigned a value as soon as my_car is created.
print(my_car.condition)
#Calling class member variables works the same whether those values are created within the class (like our car's condition) or values are passed into the new object at initialization. We use dot notation to access the member variables of classes since those variables belong to the object.  new_object.new_variable
print(my_car.model)
print(my_car.color)
print(my_car.mpg)
#A single print command that displays the result of calling my_car.display_car()
my_car.display_car()
print(my_car.drive_car())
#create an electric car named "my_car" with a "molten salt" battery_type. Supply values of your choice for the other three inputs (model, color and mpg).
my_car = ElectricCar("Ford","black",95,"molten salt")
my_car.display_electriccar()
print(my_car.drive_car())

#side note.  It seems __init__() is initializing the variables only.  It's best to create another function to print out, calculation, do any action inside the class.

#Usually, classes are most useful for holding and accessing abstract collections of data.
#One useful class method to override is the built-in __repr__() method, which is short for representation
#by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a print statement).
class Point3D(object):
	def __init__(self,x,y,z):
		self.x = x
		self.y = y 
		self.z = z
	def __repr__(self):
		return (("%s, %s, %s") % (self.x, self.y, self.z))

my_point = Point3D("a","b","c")
print(my_point)