class Dog:
    species = "pitbull"
    def __init__(self, name, age, breed): #inits
        self.name = name
        self.age = age
        self.breed = breed
    def __str__(self):
        return self.name + " is a " + str(self.age) + " years old " + self.species
    def bark(self): #methods
        print(self.name+" barks")
    

class Bulldog(Dog):
    def speak(self, sound="Bruh"):
        return f"{self.name} barks {sound}"
    
goldy = Bulldog("thomas", 25, "dope ass human")
print(goldy.speak())