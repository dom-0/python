class User(object):
    import json
    """User data"""

    def __init__(self, **more):
	for key, value in more.items():
		self.fname = key
		self.lname = value
		self.fullname = self.fname + " " + self.lname

    def storeuser (self, filename="../files/userfile.txt"):
	with open (filename, 'w') as FWH:
	    self.json.dump (self.fullname, FWH)
	    print (self.fullname + " added into the system")

    def finduser (self, filename="../files/userfile.txt"):
	with open (filename) as FRH:
 	    username = self.json.load (FRH)
        return (username)
	    
