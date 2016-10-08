class Ccoo(object):
    def __init__(self):
        self.lname = "Sen"

    def pfname(self):
        return ("Your name is " + self.lname)

fname = "A"
iname = Ccoo()
mes = iname.pfname()
print (fname + mes)
