# class contains all the code to creat objects
# name of class should start uppercase

class Animal:
    def __init__(self, species, weight, predator):
        self.species = species
        self.weight = weight
        self.predator = predator

    def animalFunc(self):
        print("The animal is: " + str(self.species))
        print("The weight is: " + str(self.weight))
        print("Is it a predator?: " + str(self.predator))
        
    def extinct(self):
        print("isn't extinct")


animalWolf = Animal("Canis Lupus", 45, True)
animalRabbit = Animal("Oryctolagus Cuniculus", 4, False)

print("==============Rabbit=================")
animalRabbit.animalFunc()
print("===============Wolf==================")
animalWolf.animalFunc()
print("=========Preservation Status=========")

listAnimals = [animalWolf, animalRabbit]
for animal in listAnimals:
    print(animal.species + ": ")
    animal.extinct()