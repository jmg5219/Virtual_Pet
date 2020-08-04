#Creating a class Pet
class Pet:
    #Using the constructor to build instances
    #Self points to the instance to use it's own attribute values
    #As with regular functions, we can define default argument values:
    def __init__(self, name, fullness=50, happiness=50,hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger #Configurable 
        self.mopiness = mopiness
    # But the real power of classes is the ability to define custom methods that make use of those attribute values.
    #Each method below modifies the instances attributes accordingly
    #the first parameter is self, which is how the body of the method access the instance.
    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    #Practicing good encapsulation is a matter of deciding the minimum amount of information an object needs to store in its state in order to do its work via its behaviors.
    #Modifying be_alive() so that it the amounts are parameterized:
    def be_alive(self, hunger, mopiness):
        self.fullness -= hunger#Parameterized
        self.happiness -= mopiness  
#Instances of the Pet class
#When we create new Pet instances, we pass in the values for the attributes:
benji = Pet("Benji", 50, 20, 20, 1)
lassie = Pet("Lassie", 50, 20, 20, 1)
clifford = Pet("Old Yeller", 50, 20, 20, 1)