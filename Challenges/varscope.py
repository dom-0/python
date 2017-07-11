a = 10
b = 12

def call_func(a, b):
    print("from inside func")
    a = 100
    b = 200
    print(a, b)

print("before calling func")
print(a, b)

call_func(a, b)

print("after calling func")
print(a, b)