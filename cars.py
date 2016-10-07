def cars (company, model, **extra_vars):
    print (model + "\t" + company )
    for key,value in extra_vars.items():
        print ("\t" + key + "\t\t" + value)
    print "\n"

cars("BMW", "X5")
cars("Mercedes", "SVR4", NO2='Yes', Engraved='With Name')
