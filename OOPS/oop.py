class Kettle(object):

    power_source = "electricity" \
                   ""
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("kenwood", 13.55)
hamilton = Kettle("hamilton", 19.99)
print("Kettles: {0.make} = {0.price} and {1.make} = {1.price}".format(kenwood, hamilton))


print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 1.5
print(kenwood.power)

print ("{} {} {}".format(Kettle.power_source, kenwood.power_source, hamilton.power_source))