class Restaurant():
    """Class for restaurant statistics"""

    def __init__(self):
	self.stat = {}

    def checkin(self, people, timing="Unknown"):
        self.stat[timing] = people

    def pstats(self):
	for time in sorted(self.stat):
		print ("At " + time + "\t\t" + self.stat[time])

    def tstats(self):
        list = []
	for num in (self.stat).values():
            list.append(int(num))
        return (sum(list))

xxx = Restaurant()
message = ""
while message != "quit":
    hour = raw_input ("Enter time: ")
    num = raw_input ("Enter number: ")
    if hour == "quit" or num == "quit":
         break
    xxx.checkin(str(num),str(hour))

print ("Summary\n-=-=-=-=-=-=-")
xxx.pstats()
print ("Total Users\n-=-=-=-=-=-=-=")
print (xxx.tstats())
