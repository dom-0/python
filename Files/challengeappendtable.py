with open("cities.txt", 'a') as cities_file:
    for i in range(1, 13):
        print("{0:0>3} times 2 is {1}".format(i, i*2), file=cities_file)
    print('-' * 30, file=cities_file)