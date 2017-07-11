imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))


print("""Album:\t{0}
Artist:\t{1}
Year:\t{2}
Tracks:""".format(imelda[0], imelda[1], imelda[2]))
for trackDetails in imelda[3]:
    print("\t{0}".format(trackDetails[1]))
