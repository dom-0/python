class Cars(object):
    """Main Cars Class"""

    def __init__(self, company, model):
	self.model = model
	self.company = company


    def desc (self):
	return (self.model + " is from the company: " + self.company)


class ElectricCars(Cars):
    """Inherited Class"""


    def __init__(self, company, model):
	super(ElectricCars, self).__init__(company,model)
	self.battery = Battery()

    def battery_info(self, size):
	return(self.battery.desc(size))

class Battery(object):
    """Another class for Battery"""

    def desc(self, size):
	return ("The size of the battery is " + str(size))

