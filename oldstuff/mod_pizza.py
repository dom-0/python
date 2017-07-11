def make_pizza (size, *toppings):
    """Description of the pizza we are about to make"""
    if len(toppings) > 0:
        print ("\nMaking a " + str(size) + " inches pizza with the following toppings:")
        for top in toppings:
            print ("\t- " + top)
    else:
        print ("\nMaking a " + str(size) + " inches pizza with default toppings")

