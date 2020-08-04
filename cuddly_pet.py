from virtual_pet import Pet
from toy import Toy
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
        for toy in self.toys:
            self.happiness += toy.use()
    #New method defined inside the sub-class
    def cuddle(self, other_pet):
        other_pet.get_love()
    #We know that in an instance of CuddlyPet, we have access all the properties and methods of Pet. And now we know that CuddlyPet can implement its own new methods.
    # But what if we wanted be_alive() to have a different effect in CuddlyPet than it does in Pet?

benji = CuddlyPet("Benji", 50, 20, 20, 1)
cujo = Pet("Cujo", 50, 10, 30, 10)
print(cujo.happiness)
# 10
benji.cuddle(cujo)
print(cujo.happiness)
# 40