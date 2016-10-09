#!/usr/bin/env python

import mod_username

nname = raw_input ("Please enter your first name: ")
lname = raw_input ("Please enter your last name: ")
dict = {nname: lname}
user = mod_username.User(**dict)

user.storeuser("./userfile")
