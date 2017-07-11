class Dog():

    def __init__(self, name, age=9):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " is sitting now")

    def old(self):
        print(self.name + " is now " + str(self.age) + " years old")

    def whatdog(self):
        print(self.name + " is a " + self.breed)


if __name__ == "__main__":

    mydog = Dog("Woof")
    mydog.sit()
    mydog.old()
    mydog.breed = "hound"
    mydog.whatdog()