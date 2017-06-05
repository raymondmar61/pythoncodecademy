#Python is an object-oriented programming language, which means it manipulates programming constructs called objects. You can think of an object as a single data structure that contains data as well as functions; functions of objects are called methods.
#Check out the code in the editor to the right. We've defined our own class, Fruit, and created a lemon instance.
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")
lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()

#A basic class consists only of the class keyword, the name of the class, and the class from which the new class inherits in parentheses.
#pass is useful as a placeholder in areas of your code where Python expects an expression.
#__init__(). This function is required for classes, and it's used to initialize the objects it creates. __init__() always takes at least one argument, self, that refers to the object being created. You can think of __init__() as the function that "boots up" each object the class creates.  Remember to start with def.
#self. This is a Python convention. It's overwhelmingly common to use self as the first parameter in __init__().
#Self is the first parameter passed to __init__(). Python will use the first parameter that __init__() receives to refer to the object being created; this is why it's often called self, since this parameter gives the object being created its identity.
#We can access attributes of our objects using dot notation.
class Animal(object):
	def __init__(self, name):
		self.name = name
zebra = Animal("Jeffrey")
print(zebra.name)

#The first argument __init__() gets is used to refer to the instance object, and by convention, that argument is called self. If you add additional arguments—for instance, a name and age for your animal—setting each of those equal to self.name and self.age in the body of __init__() will make it so that when you create an instance object of your Animal class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.
# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

#When a class has its own functions, those functions are called methods. You've already seen one such method: __init__(). But you can also define your own methods!
#Add a method, description, to your Animal class. Using two separate print statements, it should print out the name and age of the animal it's called on. Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
    	print(self.name)
    	print(self.age)
    	print(self.health) #need self. keyword for the class member variable health
hippo = Animal("Jake","5")
hippo.description()
sloth = Animal("Slim","10")
sloth.description()
ocelot = Animal("Otto","20")
ocelot.description()

#The code below is a more realistic demonstration.  We have a basic ShoppingCart class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.
#Create an instance of ShoppingCart called my_cart. Initialize it with any values you like, then use the add_item method to add an item to your cart.
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")
    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")
my_cart = ShoppingCart("Roger")
my_cart.add_item("Ukelele",10)

#Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship
#For example, a Panda is a bear, so a Panda class could inherit from a Bear class.
#However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class.  Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.
#We've defined a class, Customer, as well as a ReturningCustomer class that inherits from Customer. Note that we don't define the display_cart method in the body of ReturningCustomer, but it will still have access to that method via inheritance.
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id
    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")
class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")
monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#In Python, inheritance works like this: class DerivedClass(BaseClass): #code goes here
#where DerivedClass is the new class you're making and BaseClass is the class from which that new class inherits.
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
class Triangle(Shape):
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

#Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to override one or more of them.
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print("Hello, %s" % other.name)
class CEO(Employee):
    def greet(self, other):
        print("Get back to work, %s!" % other.name)
#Rather than have a separate greet_underling method for our CEO, we override (or re-create) the greet method on top of the base Employee.greet method. This way, we don't need to know what type of Employee we have before we greet another Employee.
ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo) # Hello, Emily. def greet Emily in employee class
ceo.greet(emp) # Get back to work, Steve!.  def greet Steve in CEO class

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
class PartTimeEmployee(Employee):
	def calculate_wage(self, hours):
		#Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.
		self.hours = hours
		return hours * 12.00
	def full_time_wage(self, hours):
		return super(PartTimeEmployee, self).calculate_wage(hours)
milton = PartTimeEmployee("Man")
print(milton.full_time_wage(10))
#On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that you've overwritten a method or attribute defined in that class' base class (also called a parent or superclass) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in "super" call:
# class Derived(Base):
#    def m(self):
#        return super(Derived, self).m()

class Triangle(object):
	number_of_sides = 3
	def __init__(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
	def check_angles(self):
		if (self.angle1 + self.angle2 + self.angle3 == 180):
			return True
		else:
			return False
class Equilateral(Triangle):
	angle = 60
	def __init__(self):
		#set self.angle1, self.angle2, and self.angle3 equal to self.angle (since an equilateral triangle's angles will always be 60˚)
		self.angle1 = self.angle
		self.angle2 = self.angle
		self.angle3 = self.angle
my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
