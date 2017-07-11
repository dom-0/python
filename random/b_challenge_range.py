iteration = input()

for i in range(int(iteration)):
    num1, num2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    temp_set = set(range(num1, num2+1))
    