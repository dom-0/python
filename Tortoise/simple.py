nameList = (("Arnab", "Sen"), ("Kabir", "Bedi"), ("Disco", "Dandiya"), ("Robert", "Cunninham"))

for name in sorted(nameList, key=lambda x: x[1]):
    print(name)