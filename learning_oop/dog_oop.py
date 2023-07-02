class Dog:
    def __init__(self, breed, name, colour, food):
        self.breed = breed
        self.name = name
        self.colour = colour
        self.food = food

    def bark(self):
        if self.breed == "Bulldog":
            print("WOOF!")
        else:
            print("woof!")

    def display_information(self):
        print("Dog breed: {}".format(self.breed))
        print("Dog name: {}".format(self.name))
        print("Colour of fur: {}".format(self.colour))
        print("Favourite food: {}".format(self.food))

    def get_favourite_food(self):
        return self.food

    def eat(self, meal):
        if meal == self.food:
            print("Mmm...")
        else:
            print("*vomit*")

sandy = Dog("Labrador Retriever", "Sandy", "Blonde", "Leftovers")
sandy.display_information()
sandy.eat(sandy.get_favourite_food())
sandy.bark()



