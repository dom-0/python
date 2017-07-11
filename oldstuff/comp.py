

def make_designs():
    while submitted_designs:
        merk = submitted_designs.pop()
        print ("Making " + merk)

        completed_designs.append(merk)

def print_done():
    print ("The list of completed designs are " + str(completed_designs))


submitted_designs = ["iphone", "robot", "dodecahedron"]
completed_designs = []
make_designs()
print_done()
