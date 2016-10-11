def cars (company, model="SX4", **extra_vars):
    print (model + "\t" + company )
    for key,value in extra_vars.items():
        print ("\t" + key + "\t\t" + value)
    print "\n"

cars("BMW", "X5", NO2='NO')
cars("Mercedes", "SVR4", NO2='Yes', Engraved='With Name')
