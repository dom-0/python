toppings = ["extra cheese", "peperoni", "salami"]
user_requests = ["peperoni", "fries", "Salami"]

for user_request in user_requests:
    if user_request.lower() in toppings:
        print ("Added " + user_request)
    else:
        print ("Weird request, you do not add '" + user_request + "' in a pizza")

list = [x.title() for x in toppings]
print (list)
