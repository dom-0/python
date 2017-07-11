class Restaurant(object):
    """A simple class to model a restaurant"""


    def __init__(self, name, cuisine="Multi"):
        self.name = name
        self.cuisine = cuisine

    def open_restaurant(self):
        print (self.name + " restaurant is open")


    def describe_restaurant(self):
        print ("The restaurant serves " + self.cuisine + " food!")



fav_eatery = Restaurant("Tadiem","Moroccan")
another_eatery = Restaurant("Kuku's")

print (fav_eatery.name)
fav_eatery.describe_restaurant()
print (another_eatery.name) 
another_eatery.describe_restaurant()


fav_eatery.open_restaurant()

another_eatery.open_restaurant()


