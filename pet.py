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
        self.toys = []
    # But the real power of classes is the ability to define custom methods that make use of those attribute values.
    #Each method below modifies the instances attributes accordingly
    #the first parameter is self, which is how the body of the method access the instance.
    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    def get_toy(self, toy):
        self.toys.append(toy)
    #Practicing good encapsulation is a matter of deciding the minimum amount of information an object needs to store in its state in order to do its work via its behaviors.
    #Modifying be_alive() so that it the amounts are parameterized:
    def be_alive(self, hunger, mopiness):
        self.fullness -= hunger#Parameterized
        self.happiness -= mopiness
        for toy in self.toys:
            self.happiness += toy.use() 
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness) 


class CuddlyPet(Pet):
    #Super fnction - we can override __init()__ while also reusing the __init__() code from the superclass.
    #With this technique, a CuddlyPet could accept additional constructor arguments:
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    #redefining a method from the parent to have different effect in the child
    #By inheritance all other methods are known by the child
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
    #New method defined inside the sub-class
    def cuddle(self, other_pet):
        other_pet.get_love()
    #We know that in an instance of CuddlyPet, we have access all the properties and methods of Pet. And now we know that CuddlyPet can implement its own new methods.
    # But what if we wanted be_alive() to have a different effect in CuddlyPet than it does in Pet?
    #Method overiding to print Extra Cuddly
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        Cuddliness: %s
        """ % (self.name, self.fullness, self.happiness,"Extra Cuddly") 

